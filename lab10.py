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
# # #zad2
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
# # #zad3
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
# #
# # #zad4
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

# names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
# ds = pd.read_csv('iris.data',names=names)
# print(ds)
# data = ds.iloc[:, :-1].values
# x = data[:,0]
# y = data[:,1]
# sss = np.abs(data[:,0] - data[:,1])
# col = np.random.randint(0,50,len(data))
# plt.scatter(x,y, c=col, s=sss*5)
# plt.colorbar()
# plt.show()

#zad6
df = pd.read_excel('imiona.xlsx')
up = df.groupby('Plec')['Liczba'].sum()
plt.subplot(1,3,1)
plt.bar(up.index,up.values, color=['red', 'blue'])
plt.title('Ogólna ilość dzieci od płci')
plt.subplot(1,3,2)
up2 = df.groupby(['Plec','Rok'])['Liczba'].sum()
plt.title('Ilość K i M w roku')
k = up2.K
m = up2.M
plt.plot(k.index, k.values, 'r-', m.index, m.values, 'b-')
plt.xticks(k.index, rotation=50)
# plt.plot(up2.index, up2['K'], color='red',label='kobiety')
# plt.plot(up2.index, up2['M'], color='blue',label='mężczyźni')
plt.subplot(1,3,3)
plt.title('Dzieci w roku')
up3 = df.groupby('Rok')['Liczba'].sum()
plt.bar(up3.index, up3.values, color='green')
plt.tight_layout()
plt.show()
#
# #zad7
# def rzucaj(n):
#     wyniki = np.zeros(n)
#     for i in range(n):
#         rzut1 = np.random.randint(1,7)
#         rzut2 = np.random.randint(1,7)
#         wyniki[i] = rzut1+rzut2
#     plt.hist(wyniki,bins=np.arange(2,14)-0.5, facecolor='g', density=True,rwidth=0.5)
#     plt.grid(True)
#     plt.xticks(np.arange(2,13))
#     plt.xlabel('Suma oczek')
#     plt.ylabel('Liczba wystąpień')
#     plt.title(f'Histogram {n} rzutów dwiema kostkami d6')
#     plt.show()
# rzucaj(1000)
#
# #zad8
# dt = pd.read_csv('zamowienia.csv', delimiter=';')
#
# sz = dt.groupby('Sprzedawca')['Utarg'].sum()
# plt.pie(sz, labels=sz.index, autopct=lambda pct: "{:.1f}%".format(pct))
# plt.show()

