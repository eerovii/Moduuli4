suuri = pieni = luku = input('Anna jokin luku: ')
while ((luku.strip('-')).replace('.', '')).isnumeric():
    if float(luku)<float(pieni):
        pieni=float(luku)
    elif float(luku)>float(suuri):
        suuri=float(luku)
    luku=input('Anna luku: ')
    #printataan stringien ääripäät
    print('Suurin antamasi luku: ' + str(suuri) + '\nPienin antamasi luku: ' + str(pieni))
