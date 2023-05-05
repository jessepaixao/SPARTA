import pickle
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import LIRU_GP as GP
import time

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
label_size=24

plt.rcParams['axes.labelsize'] = label_size
plt.rcParams['xtick.labelsize'] = label_size 
plt.rcParams['ytick.labelsize'] = label_size 
plt.rcParams['ytick.major.pad'] = label_size 
plt.rcParams['xtick.major.pad'] = label_size 
plt.rcParams['axes.labelpad'] = 32
#plt.rcParams['xtick.major.pad'] = 10
#plt.rcParams['ztick.labelsize'] = label_size 
plt.rcParams['figure.figsize'] = (8*1.5, 6*1.5)
plt.rcParams['figure.autolayout']= False

list_files=['20230228_2332_data','20230301_0009_data','20230301_0057_data','20230301_0156_data']
#list_files=['20230301_1458_data']
X =  []
Y = []

scale_vib=125

for file_name in list_files:
    
    print(file_name)
    
    # Read data
    with open('../data_experiments/'+file_name, "rb") as file_pi:
         data = pickle.load(file_pi)

    freq_list=data['freq_list']
    stack_list=data['stack_list']
    rms_vib=data['rms_vib']
    rms_pzt1=data['rms_pzt1']
    rms_pzt2=data['rms_pzt2']
        
    mesh_freq, mesh_stack = np.meshgrid(freq_list, stack_list)
    opt_vib=np.argmin(rms_vib,axis=1)
    opt_pzt1=np.argmin(rms_pzt1,axis=1)
    opt_pzt2=np.argmin(rms_pzt2,axis=1)
        
    
    # for i in range(len(freq_list)):
    #     X.append([freq_list[i], rms_pzt1[i,opt_pzt1[i]]])
    #     Y.append(stack_list[opt_pzt1[i]])
        
    for i in range(len(freq_list)):
        for j in range(len(stack_list)):
          X.append([freq_list[i], stack_list[j]])
          Y.append(rms_pzt1[i,j])
        
    
    del data
        
X=np.array(X)
Y=np.array(Y)
            
N=Y.size

print('start training')
   
# Train GP
L0 = 0.5        # Initial length scale
Sigma0 = 0.1    # Initial noise standard deviation
L, Sigma, K, C, InvC, elapsed_time = GP.Train(L0, Sigma0, X, Y, N)  # Train GP

print(elapsed_time)

# Make some predictions
N_Star = 100   # Predictions will be distributed across a 30x30 grid
f_star = np.linspace(70, 85, N_Star)             # Input points
s_star = np.linspace(0, 5, N_Star) 
X_star1, X_star2 = np.meshgrid(f_star, s_star)  # Form mesh grid for X_star
Y_StarMean = np.zeros([N_Star, N_Star])         # mean of GP predictions
Y_StarStd = np.zeros([N_Star, N_Star])          # std of GP predictions
for i in range(N_Star):
    for j in range(N_Star):
        x_star = [X_star1[i, j], X_star2[i, j]]
        Y_StarMean[i, j], Y_StarStd[i, j] = GP.Predict(X, x_star, L, Sigma,
                                                        Y, K, C, InvC, N)
        
stack_star=np.arange(0,5,0.1)
freq_star=75*np.ones(stack_star.size)
x_star=np.stack((freq_star,stack_star))
x_star=x_star.T.tolist()

Z_StarMean=[]
for x in x_star:
    mean, dev = GP.Predict(X, x, L, Sigma,
                                                        Y, K, C, InvC, N)
    Z_StarMean.append(mean)
    
stack_min=stack_star[np.argmin(Z_StarMean)]
        
# Plot Results
fig = plt.figure()
ax = plt.axes(projection ='3d')
#ax.plot_wireframe(X_star1, X_star2, Y_StarMean, label='GP mean prediction')
surf = ax.plot_surface(X_star1, X_star2, Y_StarMean,alpha=0.9, cmap=cm.Greens,label='GP mean prediction')
surf._facecolors2d=surf._facecolors3d
surf._edgecolors2d=surf._edgecolors3d
#surf = ax.scatter(mesh_freq, mesh_stack, rms_pzt1.T, color='r')
ax.scatter(X[:,0], X[:,1], Y, color='black', label='Training data',s=10)
# ax.plot(freq_star, stack_star, Z_StarMean, color='red',linewidth = 3, label='Frequency = 79')
# ax.plot(freq_star[np.argmin(Z_StarMean)], stack_min, np.min(Z_StarMean), 'bo', label='Minimum point')
ax.view_init(30, -120)
# ax.view_init(40, -30)
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Stack Voltage [V]')
ax.set_zlabel('RMS Voltage [V]',labelpad=40)
# plt.legend(fontsize=24,loc='upper left')
plt.savefig('../paper/figures/GPR_trained.png')
plt.show()

fig = plt.figure()
ax = plt.axes(projection ='3d')
#ax.plot_wireframe(X_star1, X_star2, Y_StarMean, label='GP mean prediction')
surf = ax.plot_surface(X_star1, X_star2, Y_StarMean, cmap=cm.Greens,alpha=0.9,label='GP mean prediction')
surf._facecolors2d=surf._facecolors3d
surf._edgecolors2d=surf._edgecolors3d
#surf = ax.scatter(mesh_freq, mesh_stack, rms_pzt1.T, color='r')
#ax.scatter(X[:,0], X[:,1], Y, color='black', label='Training data')
ax.plot(freq_star, stack_star, Z_StarMean, color='red',linewidth = 3, label='GP(Freq,:)')
ax.plot(freq_star[np.argmin(Z_StarMean)], stack_min, np.min(Z_StarMean), 'bo', label='Minimum point')
ax.view_init(30, -120)
# ax.view_init(40, -30)
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Stack Voltage [V]')
ax.set_zlabel('RMS Voltage [V]',labelpad=40)
plt.legend(fontsize=24,loc='upper left')
plt.savefig('../paper/figures/GPR_trained_freq_test.png')
plt.show()


# Validation of GPR
list_files=['20230301_0426_data']
X_test =  []
Y_test = []

for file_name in list_files:
    
    print(file_name)
    
    # Read data
    with open('../data_experiments/'+file_name, "rb") as file_pi:
         data = pickle.load(file_pi)

    freq_list=data['freq_list']
    stack_list=data['stack_list']
    rms_vib=data['rms_vib']
    rms_pzt1=data['rms_pzt1']
    rms_pzt2=data['rms_pzt2']
        
    mesh_freq, mesh_stack = np.meshgrid(freq_list, stack_list)
    opt_vib=np.argmin(rms_vib,axis=1)
    opt_pzt1=np.argmin(rms_pzt1,axis=1)
    opt_pzt2=np.argmin(rms_pzt2,axis=1)
        
    
    for i in range(len(freq_list)):
        for j in range(len(stack_list)):
          X_test.append([freq_list[i], stack_list[j]])
          Y_test.append(rms_pzt1[i,j])
        
    
    del data
        
X_test=np.array(X)
Y_test=np.array(Y)
            
N=Y_test.size

# Make some predictions
Y_StarMean_Test = np.zeros(X_test.shape[0])         # mean of GP predictions
Y_StarStd_Test = np.zeros(X_test.shape[0])          # std of GP predictions
for i in range(X_test.shape[0]):
    x_star = [X_test[i, 0], X_test[i, 1]]
    Y_StarMean_Test[i], Y_StarStd_Test[i] = GP.Predict(X, x_star, L, Sigma,
                                                        Y, K, C, InvC, N)
    
RMSE = np.sqrt(np.sum(np.abs(Y_StarMean_Test-Y_test)**2)/Y_test.size)

print(RMSE)
      
