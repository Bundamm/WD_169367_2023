import numpy as np
#zad1
a = np.arange(2, 41, 2)
print(a)
#zad2
b = [3.4,43.1,45.8,46.8]
m = (np.array(b, dtype='int64')).tolist()
print(m)
print(type(m))
#zad3
def fun(n):
    tab = np.arange(1,n*n+1).reshape(n,n)
    return tab
print(fun(7))
print(type(fun(7)))
#zad4
def fun2(n,m):
    t = np.logspace(start=1, stop=m, num=m, base=n,dtype=int)
    return t
print(fun2(4,10))
#zad5
def fun3(n):
    vec = np.arange(n, 0, -1)
    diag = np.diag([a for a in vec])
    return diag
print(fun3(7))
#zad6
# z= np.mgrid[0:5]
# m = 'malina'
# l = 'lizak'
# ad = 'adogaj'
# m2 = np.array(list(m))
# l2 = np.array(list(l))
# ad2 = np.array(list(ad))
#
# diag = np.diag(['' for a in m2])
# x = ''
# for i in diag:
#     for j in i:
#         x = m2[i]
# print(diag)
