import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# f(x) = 1/x, x, f(x)
# zakres osi (0,1)
# oraz (1 długość wektora x) x należy do <1,20>

# #zad1
# x = np.linspace(1,20)
# y = 1/x
# plt.plot(x,y, label='f(x) = 1/x')
# plt.title('f(x) = 1/x')
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.legend()
# plt.axis([1,20,0,1])
# plt.show()
#
# #zad2
# x = np.arange(1,21,1)
# y = 1/x
# plt.plot(x, y, 'g-->', label='f(x) = 1/x')
# plt.title('f(x) = 1/x')
# plt.ylabel('f(x)')
# plt.xlabel('x')
# plt.legend()
# plt.axis([1,20,0,1])
# plt.show()
#
# #zad3
# x = np.arange(0,31,0.1)
# s = np.sin(x)
# c = np.cos(x)
# plt.plot(x,s, 'g', label="f(x) = sin(x)")
# plt.plot(x,c, 'b', label="f(x) = cos(x)")
# plt.title('cos i sin dla x')
# plt.ylabel('sin(x) i cos(x)')
# plt.xlabel('x')
# plt.axis([1,30,-1,1])
# plt.legend()
# plt.show()
#
# #zad4
# x = np.arange(0,30.1,0.1)
# s = -np.sin(x)
# s2 = np.sin(x)+2
# plt.plot(x,s, 'orange', label='sin(x)')
# plt.plot(x,s2,label='cos(x)')
# plt.ylabel('sin(x)')
# plt.xlabel('x')
# plt.title('Wykres sin(x), sin(x)')
# plt.axis([-1,31,-1.2,3.2])
# plt.legend()
# plt.show()

#zad5

names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
ds = pd.read_csv('iris.data',names=names)

data = ds.iloc[:, :-1].values
x = data[:,0]
y = data[:,1]
sss = np.abs(data[:,0] - data[:,1])
col = np.random.randint(0,50,len(data))
plt.scatter(x,y, c=col, s=sss)
plt.colorbar()
plt.show()


