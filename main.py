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

print("8 uzduotis".center(60, "_"))

def masyvo_vidurkis(skaiciu_masyvas):
    suma = masyvo_sumavimas(skaiciu_masyvas)
    kiekis = len(skaiciu_masyvas)
    vidurkis = suma / kiekis
    return vidurkis

masyvas = skaiciu_masyvas(10, 100, 5)
rez = masyvo_vidurkis(masyvas)
print("Masyvo vidurkis:", rezultatas)

print("9 uzduotis".center(60, "_"))

def spauzdinti_staciakampi(eiluciu_skaicius,zvaigz_skaicius):
    for i in range(eiluciu_skaicius):
        for i in range(zvaigz_skaicius):
            print("*", end=" ")
        print()
spauzdinti_staciakampi(10,30)

print("10 uzduotis".center(60, "_"))

def print_sakinys(sakinys):
    tarpai = sakinys.count(" ")
    simboliai = len(sakinys) - tarpai
    print("Simboliu:", simboliai)
    print("Tarpu:", tarpai)

sakinys = "Šiandien labai graži diena"
print_sakinys(sakinys)

print("11 uzduotis".center(60, "_"))

def uzkoduoti_sakini(sakinys):
    uzkoduotas = sakinys[::-1]
    return uzkoduotas

sakinys = "Šiandien labai graži diena"
rezultatas = uzkoduoti_sakini(sakinys)
print("Užkoduotas sakinys:", rezultatas)

print("12 uzduotis".center(60, "_"))

def apsukti_zodzius(sakinys):
    zodziai = sakinys.split()
    apsukti = [zodis[::-1] for zodis in zodziai]
    naujas_sakinys = " ".join(apsukti)
    print(naujas_sakinys)

apsukti_zodzius("Labas rytas")

print("13 uzduotis".center(60, "_"))

def spausdinti_skaicius(masyvas):
    for elementas in masyvas:
        if isinstance(elementas, int):
            print(elementas)


duomenys = [7, "Labas", "123", 10, None]
spausdinti_skaicius(duomenys)

print("14 uzduotis".center(60, "_"))

def spausdinti_skaicius(masyvas):
    for elementas in masyvas:
        if isinstance(elementas, int) and not isinstance(elementas, bool):
            print(elementas)

duomenys = [7, 8, 5, 12, "Labas", "123", 10, None, 4.4]
spausdinti_skaicius(duomenys)

print("15 uzduotis".center(60, "_"))

def word_count(sakinys):
    zodziai = sakinys.split()
    suma = len(zodziai)
    return suma

sakinys = "Šiandien labai graži diena"
rezultatas = word_count(sakinys)
print("zodziu skaicius:", rezultatas)

print("16 uzduotis".center(60, "_"))


def filtruoti_skaicius(masyvas, poriniai):
    if poriniai:
        return [skaicius for skaicius in masyvas if skaicius % 2 == 0]
    else:
        return [skaicius for skaicius in masyvas if skaicius % 2 != 0]

skaiciai = [1, 2, 3, 4, 5, 6, 7, 8]

print("Poriniai:", filtruoti_skaicius(skaiciai, True))
print("Neporiniai:", filtruoti_skaicius(skaiciai, False))