# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 10:26:10 2020

@author: lab
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
'''
tab = []
with open ('dane.csv','r') as f:
    cf = csv.reader(f,delimiter=';')
    #tab = list(cf) bedzie zapisywane jako string
    for i in cf:
        #print(i)
        tab.append([int(i[0]),float(i[1]),float(i[2])])

tab = np.array(tab)

plt.plot(tab[:,0],tab[:,1],'r')
plt.plot(tab[:,0],tab[:,2],'g')
'''

tab2 = []
with open ('dane.txt','r',newline='\n') as f:
    cf = csv.reader(f,delimiter='&')
    #tab = list(cf) bedzie zapisywane jako string
    for i in cf:
        print(i)
        tab2.append([int(i[0]),float(i[1]),float(i[2].split()[0])])