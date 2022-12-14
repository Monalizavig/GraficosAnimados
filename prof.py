import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["animation.html"] = "jshtml"
plt.rcParams['figure.dpi'] = 150  
plt.ioff()

fig = plt.figure()

def animate(k):
    plt.cla()
    t = 0.1*k
    plt.scatter(10*t, 50*t - 0.5*10*t**2)
    plt.xlim(0,120)
    plt.ylim(0,150)

anim = matplotlib.animation.FuncAnimation(fig, animate, frames=100, interval=10)

# to save the animation, uncomment the following three lines
f = r"Animacao.mp4" 
writervideo = matplotlib.animation.FFMpegWriter(fps=60) 
anim.save(f, writer=writervideo,dpi =150)
