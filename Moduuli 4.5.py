tries=0
while tries<5 and (input('Käyttäjä: ')!='python' or input('Salasana: ')!='rules'):
    #määritetyt läpipääsyn ehdot
    tries+=1
if tries<5:
    #yrityskerrat
    print('Tervetuloa!')
else:
    print('Pääsy evätty.')
