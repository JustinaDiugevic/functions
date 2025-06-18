import random

print("1 uzduotis".center(60, "_"))

def suma(a,b):
    return a + b
res = suma(2,3)
print(res)

print("2 uzduotis".center(60, "_"))

def PISq():
    return 9.8596
print(PISq())

print("3 uzduotis".center(60, "_"))

def sumavimas(a,b):
    return a + b
res = sumavimas(10,20)
print(res)

print("4 uzduotis".center(60, "_"))


def spausdink_masyva(masyvas):
    for i in masyvas:
        print(i, end=' ')

spausdink_masyva([1, 2, 3, 4, 5])
print()

print("5 uzduotis".center(60, "_"))


def skaiciu_generatorius(min, max):
    return random.randint(10, 100)


rez = skaiciu_generatorius(10, 100)
print (rez)

print("6 uzduotis".center(60, "_"))

def skaiciu_masyvas(min, max, len):
    masyvas = []
    for _ in range(len):
        skaicius = random.randint(min, max)
        masyvas.append(skaicius)
    return masyvas

rez = skaiciu_masyvas(10, 100, 5)
print("Sugeneruoti skaiciai:", rez)

print("7 uzduotis".center(60, "_"))

def masyvo_sumavimas(skaiciu_masyvas):
    suma = sum(skaiciu_masyvas)
    return suma

masyvas = skaiciu_masyvas(10, 100, 5)


rezultatas = masyvo_sumavimas(masyvas)
print("Masyvo suma:", rezultatas)
