import pickle
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
label_size=28

plt.rcParams['axes.labelsize'] = label_size
plt.rcParams['xtick.labelsize'] = label_size 
plt.rcParams['ytick.labelsize'] = label_size 
plt.rcParams['ytick.major.pad'] = label_size 
plt.rcParams['xtick.major.pad'] = label_size 
plt.rcParams['axes.labelpad'] = 40
#plt.rcParams['xtick.major.pad'] = 10
#plt.rcParams['ztick.labelsize'] = label_size 
plt.rcParams['figure.figsize'] = (8*1.5, 6*1.5)
plt.rcParams['figure.autolayout']= False


# Read data
with open('../data_experiments/20230228_2332_data', "rb") as file_pi:
     data = pickle.load(file_pi)

freq_list=data['freq_list']
stack_list=data['stack_list']
rms_vib=data['rms_vib']
rms_pzt1=data['rms_pzt1']
rms_pzt2=data['rms_pzt2']
temp_vib=data['temp_vib']
temp_pzt2=data['temp_pzt2']

  
    
mesh_freq, mesh_stack = np.meshgrid(freq_list, stack_list)
opt_vib=np.argmin(rms_vib,axis=1)
opt_pzt1=np.argmin(rms_pzt1,axis=1)
opt_min_pzt2=np.argmin(rms_pzt2,axis=1)
opt_max_pzt2=np.argmax(rms_pzt2,axis=1)

scale_vib=125
rms_vib=rms_vib*1/np.sqrt(2)*scale_vib

    
fig, ax = plt.subplots(1,1)
ax = plt.axes(projection ='3d')
surf = ax.plot_surface(mesh_freq, mesh_stack, rms_vib.T, cmap=cm.Blues, alpha=0.95)
# ax.scatter(mesh_freq, mesh_stack, rms_vib.T, color='k', alpha=0.95)
for i in range(0,opt_vib.size):
    ax.plot(freq_list[i],stack_list[opt_vib[i]],rms_vib[i,opt_vib[i]],'bo')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Stack Voltage [V]')
ax.set_zlabel('RMS Velocity [mm/s]',labelpad=40)
ax.view_init(30, -120)
plt.show()
plt.savefig('../figures/vib_surface.png',bbox_inches='tight')


fig, ax = plt.subplots(1,1)
fig.set_size_inches(8*1.2, 6*1.2)
surf = ax.contourf(mesh_freq, mesh_stack, rms_vib.T, cmap=cm.Blues, alpha=0.95)
# ax.scatter(mesh_freq, mesh_stack, rms_vib.T, color='k', alpha=0.95)
for i in range(0,opt_vib.size):
    ax.plot(freq_list[i],stack_list[opt_vib[i]],'bo')
fig.colorbar(surf, shrink=0.5, aspect=10, ax = [ax],location = 'right',label='RMS Velocity [mm/s]')
ax.set_xlabel('Frequency [Hz]',labelpad=3)
ax.set_ylabel('Stack Voltage [V]',labelpad=3)
# ax.xaxis.set_tick_params(labelsize=34)
# ax.yaxis.set_tick_params(labelsize=34)
plt.show()
plt.savefig('../figures/vib_contour.png',bbox_inches='tight')



fig, ax = plt.subplots(1,1)
ax = plt.axes(projection ='3d')
surf = ax.plot_surface(mesh_freq, mesh_stack, rms_pzt1.T, cmap=cm.Reds, alpha=0.95)
# ax.scatter(mesh_freq, mesh_stack, rms_pzt1.T, color='k', alpha=0.95)
for i in range(0,opt_vib.size):
    ax.plot(freq_list[i],stack_list[opt_pzt1[i]],rms_pzt1[i,opt_pzt1[i]],'ro')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Stack Voltage [V]')
ax.set_zlabel('RMS Voltage [V]',labelpad=40)
ax.view_init(30, -120)
plt.show()
plt.savefig('../figures/pzt1_surface.png',bbox_inches='tight')


fig, ax = plt.subplots(1,1)
fig.set_size_inches(8*1.2, 6*1.2)
surf = ax.contourf(mesh_freq, mesh_stack, rms_pzt1.T, cmap=cm.Reds, alpha=0.95)
# ax.scatter(mesh_freq, mesh_stack, rms_pzt1.T, color='k', alpha=0.95)
for i in range(0,opt_vib.size):
    ax.plot(freq_list[i],stack_list[opt_pzt1[i]],'ro')
fig.colorbar(surf, shrink=0.5, aspect=10, ax = [ax],location = 'right',label='RMS Voltage [V]')
ax.set_xlabel('Frequency [Hz]',labelpad=3)
ax.set_ylabel('Stack Voltage [V]',labelpad=3)
plt.show()
plt.savefig('../figures/pzt1_contour.png',bbox_inches='tight')


# fig, ax = plt.subplots(1,1)
# ax = plt.axes(projection ='3d')
# surf = ax.plot_surface(mesh_freq, mesh_stack, rms_pzt2.T, cmap=cm.Reds, alpha=0.95)
# # for i in range(0,opt_vib.size):
# #     ax.plot(freq_list[i],stack_list[opt_min_pzt2[i]],rms_pzt2[i,opt_min_pzt2[i]],'ro')
# #     ax.plot(freq_list[i],stack_list[opt_max_pzt2[i]],rms_pzt2[i,opt_max_pzt2[i]],'bo')
# ax.set_xlabel('Frequency [Hz]')
# ax.set_ylabel('Stack Voltage [V]')
# ax.set_zlabel('RMS Voltage [V]',labelpad=40)
# ax.view_init(30, -100)
# plt.show()
# plt.savefig('../paper/figures/pzt2_surface.png')


# fig, ax = plt.subplots(1,1)
# fig.set_size_inches(8*1.2, 6*1.2)
# surf = ax.contourf(mesh_freq, mesh_stack, rms_pzt2.T, cmap=cm.Reds, alpha=0.95)
# # for i in range(0,opt_vib.size):
# #     ax.plot(freq_list[i],stack_list[opt_min_pzt2[i]],'ro')
# #     ax.plot(freq_list[i],stack_list[opt_max_pzt2[i]],'bo')
# fig.colorbar(surf, shrink=0.5, aspect=10, ax = [ax],location = 'right',label='RMS Voltage [V]')
# ax.set_xlabel('Frequency [Hz]',labelpad=3)
# ax.set_ylabel('Stack Voltage [V]',labelpad=3)
# plt.show()
# plt.savefig('../paper/figures/pzt2_contour.png')



# rms_vib_norm=rms_vib/np.max(rms_vib)
# rms_pzt1_norm=rms_pzt1/np.max(rms_pzt1)
# rms_pzt2_norm=rms_pzt2/np.max(rms_pzt2)


# diff_vib_pzt2=np.abs(rms_vib_norm-rms_pzt2_norm)
# diff_vib_pzt1=np.abs(rms_vib_norm-rms_pzt1_norm)

# fig, ax = plt.subplots(1,1)
# surf=ax.contourf(mesh_freq, mesh_stack,diff_vib_pzt1.T,cmap=cm.Reds)
# fig.colorbar(surf, shrink=0.5, aspect=10, ax = [ax],location = 'right',label='(VIB - PZT 1)')
# ax.set_xlabel('Frequency [Hz]',labelpad=3)
# ax.set_ylabel('Stack Voltage [V]',labelpad=3)
# # plt.savefig('../paper/figures/diff_pzt1_contour.png')

# fig, ax = plt.subplots(1,1)
# surf=ax.contourf(mesh_freq, mesh_stack,diff_vib_pzt2.T,cmap=cm.Reds)
# fig.colorbar(surf, shrink=0.5, aspect=10, ax = [ax],location = 'right',label='(VIB - PZT 2)')
# ax.set_xlabel('Frequency [Hz]',labelpad=3)
# ax.set_ylabel('Stack Voltage [V]',labelpad=3)
# # plt.savefig('../paper/figures/diff_pzt2_contour.png')

