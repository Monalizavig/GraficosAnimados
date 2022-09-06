import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
import math as mt
plt.rcParams["animation.html"] = "jshtml"
plt.rcParams['figure.dpi'] = 100
plt.ioff()


np.sin

fig = plt.figure()

def animate(k):
    plt.cla()
    t = 0.1*k

    plt.scatter(10*t, np.tan(np.deg2rad(15)) * 10 * t - 5 * t**2)
    plt.scatter(10*t, np.tan(np.deg2rad(30)) * 10 * t - 5 * t**2)
    plt.scatter(10*t, np.tan(np.deg2rad(45)) * 10 * t - 5 * t**2)
    plt.scatter(10*t, np.tan(np.deg2rad(60)) * 10 * t - 5 * t**2)
    plt.scatter(10*t, np.tan(np.deg2rad(75)) * 10 * t - 5 * t**2)
    plt.xlim(0, 100)
    plt.ylim(0, 90)


anim = matplotlib.animation.FuncAnimation(fig, animate, frames=100, interval=10)


f = r"Animacao.mp4" 
writervideo = matplotlib.animation.FFMpegWriter(fps=60) 
anim.save(f, writer=writervideo, dpi=150)

anim
