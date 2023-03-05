#1
spacje = input("Wpisz jakies zdanie: ")
print(spacje.count(" "))
#2
lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
spl = lorem.split()
print(spl)
print(type(lorem), type(spl))
#3
# < > <= >= != == (or and)?
#4
nb = int(input("Input a number: "))
if nb < 0:
    nb *= -1
print("Absolute value of nb is:", nb)
#5
a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))
if (a > 0 and a <= 10) and (a > b or b > c):
    print("The first number is in this range and b is lesser than a, and greater than c.")
else:
    print("One or both of the conditions are not fulfilled")
#6
for i in range(0,51):
    if(i % 5 == 0):
        print(i)
#7
inp = input("Enter numbers separated by space: ").split()
liczby = [int(i) for i in inp]
print(type(liczby))
for j in range(len(liczby)):
    print(liczby[j]**2, end=' ')
#8
print("\n")
num = input("Podaj liczbe: ")
#sep = [*num]
#l = [int(i) for i in sep]
sum = 0
for i in range(len(num)):
    sum+=int(num[i])
print(sum)
9
x =""
list =[]
while x != 'end':
    x = input()
    if x.isdigit():
        list.append(x)
        print(list)
10
s = int(input("Podaj liczbe(W zakresie od 1 do 10): "))

while s > 0 or s < 11:
    print()
s = 0
while s < 1 or s > 10:
    s = int(input())
for i in range(s+1):
    print('A'*i)

#11
y = 0
while y < 3 or y > 9:
    y = int(input())
if (y % 2 == 0):
    y -= 1

#podejście z pomocą kolegi
for i in range(1, y+1, 2):
    spacje = " " * ((y-i)//2)
    o = "o"*i
    print(spacje,o, i)
for i in range(y-2, 0, -2):
    spacje = " " * ((y - i) // 2)
    o = "o" * i
    print(spacje,o,i)


#pierwsze nie działające podejście
# srodek = (1 + y)/2
# i = 1
# m = 0
# z = y
# while i <= y:
#     spacje = " " * ((y-i) // 2)
#     if i == 1:
#         print(spacje, "o")
#         i += 1
#     if i < srodek:
#         m+=2
#         print(spacje, "o"*(m+1))
#         i+=1
#     if i == srodek:
#         print("o"*y)
#         i+=1
#     if i > srodek and z != i:
#         i+=1
#         z -= 2
#         print(spacje, "o" * z)