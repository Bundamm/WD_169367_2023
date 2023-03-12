import math
import random
def nowa_funkcja(argument1,argument2=1):
    argument1 = argument2
    return argument1

print(nowa_funkcja(argument1=2))

print("Podaj argumenty funkcji liniowej: ")
a = int(input())
b = int(input())

def zad1(a,b):
    if a < 0:
        print("Funkcja",a,"x +",b,"jest malejaca.")
    if a > 0:
        print("Funkcja", a, "x +", b, "jest rosnaca.")
    if a == 0:
        print("Funkcja", a, "x +", b, "jest stala.")
zad1(a,b)

print("Podaj argumenty przy x dwoch funkcji liniowych")
a1= eval(input())
a2= eval(input())
def zad2(a1,a2):
    if a1==a2:
        print("Proste sa rownolegle.")
    if a1*a2==-1:
        print("Proste sa prostopadle.")
    else:
        print("Nie sa ani rownolegle, ani prostopadle.")
zad2(a1,a2)

print("Podaj przyprostokatne: ")
a3 = eval(input())
b = eval(input())
def zad3(arg1,arg2):
    odp = math.sqrt(arg1**2 + arg2**2)
    return odp
print(zad3(a3,b))

print("Podaj pierwszy element, przejscie i ilosc elementow ciagu arytmetycznego.")
a11 = eval(input())
r = eval(input())
ile = eval(input())
def zad4(a1=1, r=1, ile=10):
    ai = a1 + (ile-1) * r
    print("a",ile," rowna sie: ",ai, sep='')
    suma = (a1 + ai)/2 * ile
    return suma

print(zad4(a11,r,ile))

lista = ["asf","awfg","asegsehjgiu"]
lista2 = ["seagsrege", "segsefg", "eafeaf"]
def dodaj_znak(arg):
    for i in range(len(arg)):
        arg[i] += "!"
    return arg
dodaj_znak(lista)
print(lista)

def dodaj_znak2(arg):
    nowa = []
    for i in range(len(arg)):
        nowa.append(arg[i]+"!")
    return nowa

print(dodaj_znak2(lista2))
print(lista2)

def guess_the_number():
    print("zgadnij liczbe w zakresie 1 do 10")
    punkty = 0
    for i in range(0,5):
        x = random.randint(1,10)
        odp = int(input())
        if(odp == x):
            print("Wylosowana liczba to: ", x, " zdobywasz 10 punktow.",sep='')
            punkty+=10
        if(odp < 1 or odp > 10):
            print("To nie jest od 1 do 10.")
            return 0
        else:
            print("Wylosowana liczba to: ", x, " tracisz 1 punkt.", sep='')
            punkty -=1
    print("Koniec gry. Twoja punktacja to: ", punkty, "punktow.")
    return 0
guess_the_number()
num = input()
def digital_root(arg):
    arg = int(arg)
    while arg >= 10:
        arg = sum(int(i) for i in str(arg))
    return arg
print(digital_root(num))
def multiply_game():
    correct = 0
    wrong = 0
    for i in range(0,10):
        x = random.randint(1,9)
        y = random.randint(1,9)
        print("Pytanie ", i+1,': ',x,' x ',y, ' = ',  sep='')
        z = int(input())
        if z == x * y:
            print("Poprawna odpowiedz!")
            correct+=1
        else:
            print("Bledna odpowiedz. Poprawna odpowiedzia jest: ", x*y, sep='')
            wrong+=1
    print("Koniec gry!\nBledne odpowiedzi: ",wrong,'\nPoprawne odpowiedzi: ',correct,sep='')
multiply_game()
print("Wprowadz wysokosc: ")
h = int(input())
j = 1
for i in range(0,h):
    spacje = " " *(h - i)
    if i==0:
        print(spacje,"*")
    else:
        spacje2 = j * " "
        if(h//2 != i):
            print(" ",spacje, "*", spacje2, "*", sep='')
        else:
            #wersja kolegi
            #print(spacje, "*"*(((i+1)*2)-1))
            #wersja moja
            if(h%2==0):
                print(spacje, "*"*(h+1))
            else:
                print(spacje, "*"*h)
        j += 2