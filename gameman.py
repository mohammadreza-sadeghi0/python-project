import random
min = 1
max = 99
hads = random.randint(min , max)
print(hads)
javab = input('javab: ')
while javab != 'd':
    if javab == 'b':
        min = hads
    elif javab == 'k':
        max = hads
    hads = random.randint(min , max)
    print(hads)
    javab = input('javab: ')
print('barandeh')
