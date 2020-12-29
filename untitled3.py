# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:35:44 2020

@author: ASUS_PEPE
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 17:22:13 2020

@author: Paweł
"""
'''
zestawienie= str(input('zestawienie: '))
lista=[]
petle= int(input('petle: '))
for k in range(0,petle):
    nazwa=str(input('nazwa: '))
    wartosc=int(input('wartosc: '))
    rok=int(input('rok: '))
    typ=str(input('typ: '))
    lista.append([nazwa,wartosc,rok,typ,k])
    print(lista)
    
with open('dane.txt','w') as f:
    for i in range(len(lista)):
        f.write(f'{lista[i]} \\\\ \\hline \n')
'''


tab2 = []
with open ('dane.txt','r',newline='\n') as f:
    cf = csv.reader(f,delimiter=',')
    for i in cf:
        print(i)
        tab2.append([str(i[0].split(',')[0])])#,int(i[0].split(',')[1]),int(i[0].split(',')[2]),str(i[0].split(',')[3]),int(i[0].split(',')[4])])
