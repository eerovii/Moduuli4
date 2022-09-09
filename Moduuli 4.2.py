tuuma=float(input('Anna mitta tuumina: '))
while tuuma>-1:
    tuuma=float(input('Anna mitta tuumina: '))
    if tuuma>=0:
        #tuuman muunnos senttimetreiksi
        print(str(tuuma*2.54) + ' senttimetriä.')
