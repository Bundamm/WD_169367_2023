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
def wykres():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    t = np.linspace(0, 2* np.pi, 100)
    z = t
    x = np.sin(t)
    y = 2* np.cos(t)
    ax.plot(x,y,z,label='zadanie 1')
    ax.legend()
    plt.show()


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

# plaszcz()

#zad4

def slupek():
    fig = plt.figure()
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    #w1
    ax1 = fig.add_subplot(221,projection='3d')
    ax1.bar3d(x,y,bottom,width,depth,top,shade=True,color='b')
    ax2 = fig.add_subplot(222, projection='3d')
    ax2.bar3d(x, y, bottom, width, depth, top, shade=False, color='g')
    ax3 = fig.add_subplot(223, projection='3d')

    ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color='hotpink', alpha=0.5)
    ax3.view_init(50,50)
    ax4 = fig.add_subplot(224, projection='3d')
    ax4.bar3d(x, y, bottom, width, depth, top, shade=False, color='darkred', alpha=0.2)
    ax4.view_init(180,180)
    plt.show()
slupek()