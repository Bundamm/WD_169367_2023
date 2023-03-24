import numpy as np

print('Zad 1')
mx1 = np.array([2, 6, 4])
mx2 = np.array([5, 4, 8])
print(mx1 * mx2)

print('Zad 2')
mak1 = np.random.randint(10, 51, size=(3, 3))
mak2 = np.random.randint(10, 51, size=(4, 4))

mk1 = np.min(mak1, axis=0)
mk1_1 = np.min(mak1, axis=1)
mk2 = np.min(mak2, axis=0)
mk2_2 = np.min(mak2, axis=1)
print(mak1, '\n', mk1, mk1_1, '\n', mak2, '\n', mk2, mk2_2)

print('Zad 3')
print(np.dot(mx1, mx2))
print(mx1.dot(mx2))

print('Zad 4')
vek1 = np.array([1, 5, 7])
vek2 = np.array([1.4, 5.8, 10.34])
print(vek1 * vek2)

print('Zad 5')
mxx = np.array(([3, 8, 7], [2, 4, 6]))
a = np.sin(mxx)
print(a)

print('Zad 6')
mxx2 = np.array(([45, 7, 4], [3, 8, 234]))
b = np.cos(mxx2)
print(b)

print('Zad 7')
print(a + b)

print('Zad 8')
mak3 = np.random.randint(10, 51, size=(3, 3))
for i in range(3):
    print(mak3[i])

print('Zad 9')
mak4 = np.random.randint(10, 51, size=(3, 3))
for i in mak4.flat:
    print(i, end=' ')

print('Zad 10')
mak5 = np.random.randint(10, 51, size=(9, 9))
for i in range(1, 82):
    for j in range(1, 82):
        if i * j == 81:
            print(mak5.reshape(i, j))
# Wszystkich mozliwosci jest 5
print('Zad 11')
mx11 = np.array([2, 6, 4, 8, 43, 23, 324, 654, 3465, 2, 34, 12])

print('3x4:')
mx11_3x4 = mx11.reshape(3, 4)
print(mx11_3x4)

print('4x3:')
mx11_4x3 = mx11.reshape(4, 3)
print(mx11_4x3)

print('2x6:')
mx11_2x6 = mx11.reshape(2, 6)
print(mx11_2x6)

print('mx11_3x4 flat:')
mx11_3x4_flat = mx11_3x4.flatten()
print(mx11_3x4_flat)

print('4x3 flat:')
mx11_4x3_flat = mx11_4x3.flatten()
print(mx11_4x3_flat)

print('2x6 flat:')
mx11_2x6_flat = mx11_2x6.flatten()
print(mx11_2x6_flat)