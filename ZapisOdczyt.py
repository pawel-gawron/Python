# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:20:21 2020

@author: ASUS_PEPE
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

k = np.arange(0,370,10)
r = np.deg2rad(k)

s = np.sin(r)
c = np.cos(r)

with open('dane1.txt','w') as f:
    for i in range(len(k)):
        f.write(f'{k[i]} & {s[i]:.2f} & {c[i]:.2f} \\\\ \\hline \n')
        
with open('dane.csv','w',newline='') as f:
    cf = csv.writer(f,delimiter=';')
    for i in range(len(k)):
        cf.writerow([k[i],f'{s[i]:.3f}',f'{c[i]:.3f}'])
        

tab2 = []
with open ('dane1.txt','r',newline='\n') as f:
    cf = csv.reader(f,delimiter='&')
    for i in cf:
        print(i)
        tab2.append([int(i[0]),float(i[1]),float(i[2].split()[0])])
        
plt.plot(k,s,'g')
plt.plot(k,c,'r')
plt.title("Wykres funkcji sinus, cosinus")
plt.xlabel("Stopnie")
plt.ylabel("Wartosć")
plt.grid()
plt.axis('tight')
plt.legend(['sin','cos'])
plt.savefig('SinusCosinus.png')