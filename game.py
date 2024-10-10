import random
a = 1
b = 99
javab = random.randint(a,b)

hads = int(input('please your hads: '))
while hads != javab:
    if hads < javab:
        print('javab bozorg tar ast')
    else:
        print('javab khocek tar ast')
    hads = int(input('please your hads: '))

print('javab dorost bood')
