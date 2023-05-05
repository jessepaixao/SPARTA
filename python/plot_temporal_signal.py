import pickle
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition, mark_inset, inset_axes

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
label_size=32

plt.rcParams['axes.labelsize'] = label_size
plt.rcParams['xtick.labelsize'] = label_size 
plt.rcParams['ytick.labelsize'] = label_size 
plt.rcParams['ytick.major.pad'] = label_size 
plt.rcParams['xtick.major.pad'] = label_size 
plt.rcParams['axes.labelpad'] = 32
plt.rcParams['xtick.major.pad'] = 10
# plt.rcParams['ztick.labelsize'] = label_size 
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['figure.autolayout']= False

# Read data
with open('../data_experiments/20230301_0426_data', "rb") as file_pi:
     data = pickle.load(file_pi)


data_temp_pzt1=data['temp_pzt1']
data_temp_pzt2=data['temp_pzt2']
data_temp_vib=data['temp_vib']

scale_vib=125
t=np.linspace(0,2,data_temp_vib.shape[2])


data_temp_vib=data_temp_vib*scale_vib


# Figure 1 - PZT 1 Voltage

fig, ax = plt.subplots(1,1)
ax.plot(t,data_temp_pzt1[0,0,:],'r')

# Zoom 1
axins1 = inset_axes(ax, 1.5,1.5 , loc=2, bbox_to_anchor=(190,750))
axins1.plot(t,data_temp_pzt1[0,0,:],'r')
axins1.set_xlim(0, 0.2)
mark_inset(ax, axins1, loc1=2, loc2=4, linewidth=0.7,alpha=0.4, fc="None", ec='k', clip_on=True, zorder=3)

# Zoom 2
axins2 = inset_axes(ax, 1.5,1.5 , loc=2, bbox_to_anchor=(490,750))
axins2.plot(t,data_temp_pzt1[0,0,:],'r')
axins2.set_xlim(1.8, 2)
mark_inset(ax, axins2, loc1=1, loc2=3, linewidth=0.7,alpha=0.4, fc="None", ec='k', clip_on=True, zorder=3)

ax.set_xlabel('Time [s]',labelpad=3)
ax.set_ylabel('PZT1 Voltage [V]',labelpad=3)
ax.set_xlim(0,2)

plt.savefig('../paper/figures/temp_pzt1.png',bbox_inches='tight')

# Figure 2 - Vibromter Velocity

fig, ax = plt.subplots(1,1)
ax.plot(t,data_temp_vib[0,0,:],'b')
# Zoom 1
axins1 = inset_axes(ax, 1.5,1.5 , loc=2, bbox_to_anchor=(190,750))
axins1.plot(t,data_temp_vib[0,0,:],'b')
axins1.set_xlim(0, 0.2)
mark_inset(ax, axins1, loc1=2, loc2=4, linewidth=0.7,alpha=0.4, fc="None", ec='k', clip_on=True, zorder=3)

# Zoom 2
axins2 = inset_axes(ax, 1.5,1.5 , loc=2, bbox_to_anchor=(490,750))
axins2.plot(t,data_temp_vib[0,0,:],'b')
axins2.set_xlim(1.8, 2)
mark_inset(ax, axins2, loc1=1, loc2=3, linewidth=0.7,alpha=0.4, fc="None", ec='k', clip_on=True, zorder=3)

ax.set_xlabel('Time [s]',labelpad=3)
ax.set_ylabel('Velocity [mm/s]',labelpad=3)
ax.set_xlim(0,2)
plt.savefig('../paper/figures/temp_vib.png',bbox_inches='tight')
#plt.show()
#plt.close()


# Figure 3 - Vibromter Velocity

fig, ax = plt.subplots(1,1)
ax.plot(t,data_temp_vib[0,0,:],'b')
ax.set_xlabel('Time [s]',labelpad=3)
ax.set_ylabel('Velocity [mm/s]',labelpad=3)
ax.set_xlim(0,0.2)
plt.savefig('../paper/figures/temp_vib_zoom.png',bbox_inches='tight')

# Figure 4 - PZT 1 Voltage

fig, ax = plt.subplots(1,1)
ax.plot(t,data_temp_pzt1[0,0,:],'r')
ax.set_xlabel('Time [s]',labelpad=3)
ax.set_ylabel('PZT1 Voltage [V]',labelpad=3)
ax.set_xlim(0,0.2)
plt.savefig('../paper/figures/temp_pzt1_zoom.png',bbox_inches='tight')

plt.show()


