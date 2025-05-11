import random
print('damam etmek ucun "y", dayanmaq ucun "n" secin')
emeliyyatlar=['+','-','*']
while True:
    secim=input("davam etmek isteyirsiz: ")
    serhed1=int(input(' hesablama ucun birinci serhedi yazin: '))
    serhed2=int(input(' hesablama ucun ikinci serhedi yazin: '))
    eded1=random.randint(serhed1,serhed2)
    eded2 = random.randint(serhed1, serhed2)
    emeliyyat=random.choice(emeliyyatlar)
    def sual_yarat():
        return str(eded1)+' '+emeliyyat+' '+str(eded2)
    def sualin_cavabi():
        if emeliyyat=='+':
            cavab=eded1+eded2
            return cavab
        elif emeliyyat=='-':
            cavab=eded1-eded2
            return cavab
        else:
            cavab=eded1*eded2
            return cavab
    def sizin_cavabiniz():
        cavabiniz=int(input('cavab daxil edin: '))
        if cavabiniz==sualin_cavabi():
            print('DOGRUDUR!')
        else:
            print('YANLISDIR!\ndogru cavab:',sualin_cavabi())
    print(sual_yarat())
    print(sizin_cavabiniz())
    if secim=="y":
        continue
    else:
        break