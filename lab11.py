from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# t = np.linspace(0,2 * np.pi, 100)
# z = x = np.sin(t) * np.cos(t)
# y = np.tan(t)
# ax.plot(x,y,z,label='zadanie 1')
# ax.legend()
# plt.show()

#zad1
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# t = np.linspace(0, 2* np.pi, 100)
# z = t
# x = np.sin(t)
# y = 2* np.cos(t)
# ax.plot(x,y,z,label='zadanie 1')
# ax.legend()
# plt.show()

#zad2
def punkty():
    pkt = 200
    x = np.random.rand(pkt)
    y = np.random.rand(pkt)
    z = np.random.rand(pkt)
    c = np.random.choice(['r','g','b','c','m'],pkt)
    m = np.random.choice(['o','s','v','*','D'],pkt)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(pkt):
        ax.scatter(x[i], y[i], z[i], c=c[i], marker=m[i])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Wykres 3D punktowy dla 5 różnych serii')
    plt.show()

#zad3

def plaszcz():
    cmaps = [cm.viridis, cm.plasma, cm.inferno, cm.magma,cm.ocean]
    for i, cmap in enumerate(cmaps):
        fig = plt.figure()
        ax = fig.add_subplot(111,projection='3d')
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)
        surf = ax.plot_surface(X, Y, Z, cmap=cmap, linewidth=0, antialiased=False)
        ax.set_zlim(-1.01,1.01)
        ax.zaxis.set_major_locator(plt.LinearLocator(10))
        ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))
        fig.colorbar(surf,shrink=0.5, aspect=5)
        plt.show()

plaszcz()