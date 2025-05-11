import random
lst=['tas', 'cagit', 'makas']

while True:
    yarismaci1=input('seciminizi edin(tas/cagit/makas):')
    yarismaci2=random.choice(lst)
    if yarismaci1==yarismaci2:
        print('BERABERE')
    else:
        if yarismaci1 == 'tas' and yarismaci2 == 'cagit':
            print(f'birinci yarisci {yarismaci1} ve ikinci yarisci {yarismaci2} qalib ise IKINCI YARIMACI')
        elif yarismaci1 == 'tas' and yarismaci2 == 'makas':
            print(f'birinci yarisci {yarismaci1} ve ikinci yarisci {yarismaci2} qalib ise BIRINCI YARIMACI')
        elif yarismaci1 == 'makas' and yarismaci2 == 'tas':
            print(f'birinci yarisci {yarismaci1} ve ikinci yarisci {yarismaci2} qalib ise IKINCI YARIMACI')
        elif yarismaci1 == 'makas' and yarismaci2 == 'cagit':
            print(f'birinci yarisci {yarismaci1} ve ikinci yarisci {yarismaci2} qalib ise BIRINCI YARIMACI')
        elif yarismaci1 == 'cagit' and yarismaci2 == 'makas':
            print(f'birinci yarisci {yarismaci1} ve ikinci yarisci {yarismaci2} qalib ise IKINCI YARIMACI')
        else:
            print(f'birinci yarisci {yarismaci1} ve ikinci yarisci {yarismaci2} qalib ise BIRINCI YARIMACI')
    secim = input("oyuna davam edirsiz?")
    if secim=='he':
        continue
    else:
        break