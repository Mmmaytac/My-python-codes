teklikler=['','bir','iki','uc','dord','bes','alti','yeddi','sekiz','dokuz']
onluqlar=['','on','yirmi','otuz','qirx','elli','altmis','yetmis','seksen','doksan']
yuzluklar=['','yuz','ikiyuz','ucyuz','dordyuz','besyuz','altiyuz','yeddiyuz','sekizyuz','dokuzyuz']
minlikler=['','min','ikimin','ucmin','dordmin','besmin','altimin','yeddimin','sekizmin','dokuzmin']
eded=input('4 reqemli eded daxil edin:')
if eded[0]=='0':
    print('',end=' ')
else:
    print(minlikler[int(eded[0])],end=' ')

if eded[1] == '0':
    print('',end=' ')
else:
    print(yuzluklar[int(eded[1])], end=' ')

if eded[2] == '0':
    print('',end=' ')
else:
    print(onluqlar[int(eded[2])], end=' ')

if eded[3] == '0':
    print('',end=' ')
else:
    print(teklikler[int(eded[3])])