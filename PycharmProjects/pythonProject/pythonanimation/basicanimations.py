import matplotlib
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

t0=0
t_end = 2
dt=0.005

t = np.arange(t0,t_end+dt,dt)
print(t)

x = 800*t

alt = 2
y = np.ones(len(t)) *alt
print(len(t))

# animation
frame_amount = len(t)
def update_plot(num):

    return
fig =plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))

gs= gridspec.GridSpec(2,2)
# subplot
ax0 =fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9))

plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount,  interval=20, repeat=True, blit=True)
plt.show()