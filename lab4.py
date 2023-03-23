import numpy as np
# #zad1
# a = np.arange(2, 41, 2)
# print(a)
# #zad2
# b = [3.4,43.1,45.8,46.8]
# m = (np.array(b, dtype='int64')).tolist()
# print(m)
# print(type(m))
# #zad3
# def fun(n):
#     tab = np.arange(1,n*n+1).reshape(n,n)
#     return tab
# print(fun(7))
# print(type(fun(7)))
# #zad4
# def fun2(n,m):
#     t = np.logspace(start=1, stop=m, num=m, base=n,dtype=int)
#     return t
# print(fun2(4,10))
# #zad5
# def fun3(n):
#     vec = np.arange(n, 0, -1)
#     diag = np.diag([a for a in vec])
#     return diag
# print(fun3(7))
# zad6
m = 'malina'
l = 'link'
ad = 'ytkefa' #afekty
al = 'snfselnf'
ad2 = ad[::-1] #pierwszy dwukropek - nie ma wartosci początkowej/końcowej a drugi - rozdielenie dwóch wartości
length = max(len(m), len(l), len(ad))

mx = np.diag([x for x in l], -2)

mx[:,0] = [x for x in m]
mx[-1,:] = [x for x in ad2]

print(mx)

#zad7
# def zad7(n):
#     wek = np.ones(n, dtype=int)*2
#     mac = np.diag(wek)
#
#     for i in range(1, n):
#         wek2 = np.ones(n - i, dtype=int) * 2 * (i + 1)
#         mac += np.diag(wek2, i) + np.diag(wek2, -i)
#     print(mac)
#
# n = int(input("Podaj wymiar macierzy: "))
# zad7(n)
#zad8
# def zad8(idk, kierunek=0):
#     if kierunek == 1 and idk.shape[1] % 2 == 0:
#             half = idk.shape[1]//2
#             new_idk1 = idk[:, :half]
#             new_idk2 = idk[:, half:]
#             print("Pierwsza polowa to: \n",new_idk1, '\n',"Druga polowa to: \n", new_idk2)
#     elif kierunek == 0 and idk.shape[0] % 2 == 0:
#             half = idk.shape[0]//2
#             new_idk1 = idk[:half]
#             new_idk2 = idk[half:]
#             print("Pierwsza polowa to: \n",new_idk1, '\n',"Druga polowa to: \n", new_idk2)
#     else:
#         print("Nie da sie")
# mat = np.arange(1,17)
# mat = mat.reshape(4,4)
# zad8(mat,0)
#zad9
# def fib(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-2) + fib(n-1)
#
# wec = np.arange(0,25)
# for i in range(0,25):
#     wec[i] = fib(i)
# wec = wec.reshape(5,5)
# print(wec)