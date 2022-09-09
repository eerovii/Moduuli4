import random
numero=random.randint(1,10)
arvaus=int(input('Arvaa arpomani numero: '))
while arvaus!=numero:
    if arvaus<numero:
        print('Arvauksesi on liian pieni.')
    elif arvaus>numero:
        print('Arvauksesi on liian suuri.')
    arvaus = int(input('Arvaa arpomani numero: '))
print('Oikein arvattu!')
