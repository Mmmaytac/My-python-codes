def toplama(eded1,eded2):
    netice=eded1+eded2
    print(f'{eded1}+{eded2}={netice}')
def cixma(eded1,eded2):
    netice=eded1-eded2
    print(f'{eded1}-{eded2}={netice}')
def vurma(eded1,eded2):
    netice=eded1*eded2
    print(f'{eded1}*{eded2}={netice}')
def bolme(eded1,eded2):
    if eded2==0.0:
        print('0-a bolmek olmaz')
    else:
        netice=eded1/eded2
        print(f'{eded1}/{eded2}={netice}')
while True:
    print('hansi emeliyyati etmek istiyiyirsiz?')
    print('toplama ucun: 1')
    print('cixma ucun: 2')
    print('vurma ucun: 3')
    print('bolme ucun: 4')
    print('emeliyyati bitirmek ucun: q')
    secim=input('seciminizi edin:')

    if secim=='q':
        print('calculatordan cixdiniz')
        break

    else:
        eded1 = float(input('birinci ededi yazin:'))
        eded2 = float(input('ikinci ededi yazin:'))
        if secim=='1':
            print(toplama(eded1,eded2))
        elif secim=='2':
            print(cixma(eded1,eded2))
        elif secim=='3':
            print(vurma(eded1,eded2))
        elif secim=='4':
            print(bolme(eded1,eded2))
        else:
            print('yalnis secim edilib')