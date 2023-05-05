import pickle
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# import LIRU_GP as GP
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition, mark_inset, inset_axes

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
label_size=24
pad_size=10

plt.rcParams['axes.labelsize'] = label_size
plt.rcParams['xtick.labelsize'] = label_size 
plt.rcParams['ytick.labelsize'] = label_size 
plt.rcParams['ytick.major.pad'] = pad_size 
plt.rcParams['xtick.major.pad'] = pad_size 
plt.rcParams['axes.labelpad'] = pad_size
plt.rcParams['figure.figsize'] = (8*1.5, 6*1.5)
plt.rcParams['figure.autolayout']= False
plt.rcParams['legend.fontsize']= 'large'
plt.rcParams['savefig.dpi'] = 300


# file_name='20230302_1051_data_GPRcontrol_on_off'
file_name='20230302_1122_data_GPRcontrol_on_off'


# Read data
with open('../data_experiments/'+file_name, "rb") as file_pi:
    data = pickle.load(file_pi)
    

scale_vib=125    


data_pzt1_on=data['data_pzt1_on']
data_pzt2_on=data['data_pzt2_on']
data_vib_on=data['data_vib_on']*scale_vib
data_stack_on=data['data_stack_on']
data_pzt1_off=data['data_pzt1_off']
data_pzt2_off=data['data_pzt2_off']
data_vib_off=data['data_vib_off']*scale_vib
data_stack_off=data['data_stack_off']


#scale_vib=126.81



T=1/2500
t=np.arange(0,data_pzt1_on.shape[0])*T

fig, ax = plt.subplots(2,1)
ax[0].plot(t,data_vib_off,alpha=1,color='b',label='Equal-peak')
ax[0].plot(t,data_vib_on,alpha=0.9,color='r',label='Adaptive control')
ax[0].set_xlabel('Time [s]')
ax[0].set_ylabel('Velocity [mm/s]')
ax[0].set_xlim(0,t[-1])



axins1 = inset_axes(ax[0], 1.5,1.5 , loc=2, bbox_to_anchor=(120*3,1050*3))
axins1.plot(t,data_vib_off,alpha=1,color='b',label='Equal-peak')
axins1.plot(t,data_vib_on,alpha=0.9,color='r',label='Adaptive control')
axins1.set_xlim(44.4, 44.7)
mark_inset(ax[0], axins1, loc1=1, loc2=2, linewidth=0.7,alpha=0.4, fc="None", ec='k', clip_on=True, zorder=3)


axins2 = inset_axes(ax[0], 1.5,1.5 , loc=2, bbox_to_anchor=(550*3,1050*3))
axins2.plot(t,data_vib_off,alpha=1,color='b',label='Equal-peak')
axins2.plot(t,data_vib_on,alpha=0.9,color='r',label='Adaptive control')
axins2.set_xlim(66.5, 66.7)
mark_inset(ax[0], axins2, loc1=1, loc2=2, linewidth=0.7,alpha=0.4, fc="None", ec='k', clip_on=True, zorder=3)

axins3 = inset_axes(ax[0], 1.5,1.5 , loc=2, bbox_to_anchor=(950*3,1050*3))
axins3.plot(t,data_vib_off,alpha=1,color='b',label='Equal-peak')
axins3.plot(t,data_vib_on,alpha=0.9,color='r',label='Adaptive control')
axins3.set_xlim(80.4, 80.7)
mark_inset(ax[0], axins3, loc1=1, loc2=2, linewidth=0.7,alpha=0.4, fc="None", ec='k', clip_on=True, zorder=3)






ax[1].plot(t,data_stack_off,alpha=1,color='b',label='Equal-peak')
ax[1].plot(t,data_stack_on,alpha=1,color='r',label='Adaptive control')
ax[1].set_xlabel('Time [s]')
ax[1].set_ylabel('Stack Voltage [V]')
ax[1].set_xlim(0,t[-1])
#plt.legend(fontsize=24)
#plt.savefig('../paper/figures/vib_GPRcontrol_120s.png',bbox_inches='tight')
plt.show()




attenuation_db=20*np.log10(np.max(data_vib_off)/np.max(data_vib_on))
attenuation_amp=(np.max(data_vib_off)-np.max(data_vib_on))/np.max(data_vib_off)*100

print('Amplitude attenuatiion [db]: ',attenuation_db)
print('Amplitude attenuatiion [%]: ',attenuation_amp)






