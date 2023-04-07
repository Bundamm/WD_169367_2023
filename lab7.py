import numpy as np
import pandas as pd
def zad7(n):
    mat = np.zeros((n,n))
    print(mat)
zad7(3)

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