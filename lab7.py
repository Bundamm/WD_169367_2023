import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
# def zad7(n):
#     mat = np.zeros((n,n))
#     for i in range(1,n+1):
#         var_r = np.diag(np.full(n-i+1,i*2), i-1)
#
#         if i > 1:
#             var_l = np.diag(np.full(n - i + 1, i * 2), -(i - 1))
#             mat += var_l
#         mat += var_r
#
#     print(mat)
# zad7(3)

# def zad8(tab,k='poziomo'):
#     if k =='poziomo':
#         if tab.shape[0] % 2 != 0:
#             print('Tablica ma nieparzysta liczbe wierszy')
#             return
#         else:
#             mat1 = tab[:int((tab.shape[0]/2))]
#             mat2 = tab[int(tab.shape[0] / 2):]
#             print("Część 1:",mat1, end='\n', sep='\n')
#             print("Część 2:", mat2, end='\n', sep='\n')
#     if k =='pionowo':
#         if tab.shape[0] % 2 != 0:
#             print('Tablica ma nieparzysta liczbe kolumn.')
#             return
#         else:
#             mat1 = tab[:,:int((tab.shape[0]/2))]
#             mat2 = tab[:,int(tab.shape[0] / 2):]
#             print("Część 1:",mat1, end='\n', sep='\n')
#             print("Część 2:", mat2, end='\n', sep='\n')
#
#
# uneven = np.arange(9).reshape(3,3)
# print(uneven)
# even = np.arange(16).reshape(4,4)
# print(even)
#
# zad8(even,k='poziomo')

data = pd.read_excel('imiona.xlsx')
print('1)')
bpy = data.groupby('Rok')['Liczba'].sum()
# y = bpy.max()
# # y = np.random.randint(100)
# ts=pd.Series(y,index=bpy)
# print(ts)
# ts = ts.cumsum()
# print(ts)
# ts.plot(x=bpy,y=y)
# plt.show()
plot = bpy.plot()
plot.set_ylabel('Ilosc')
plot.set_xlabel('Rok')
plot.legend()
plt.title('Ilosc urodzen na rok')
plt.show()
#zad2
print('2)')
bpg = data.groupby('Plec')['Liczba'].sum()
plt.bar(bpg.index, bpg.values)
plt.title('Liczba urodzen zaleznie od plci')
plt.ylabel('Liczba ur')
plt.xlabel('Plec')
plt.show()
#zad3
print('Zadanie 3')
l5y = data[data['Rok'] >= 2013]
bpg = l5y.groupby('Plec')['Liczba'].sum()
plt.pie(bpg.values, labels=bpg.index, autopct='%1.1f%%')
plt.title('Liczba urodzen chlopcow i dziewczat')
plt.show()
