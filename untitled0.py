# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 09:53:44 2020

@author: lab
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

k = np.arange(0,370,10)
r = np.deg2rad(k)

s = np.sin(r)
c = np.cos(r)

with open('dane.txt','w') as f:
    for i in range(len(k)):
        f.write(f'{k[i]} & {s[i]:.2f} & {c[i]:.2f} \\\\ \\hline \n')
        
with open('dane.csv','w',newline='') as f:
    cf = csv.writer(f,delimiter=';')
    for i in range(len(k)):
        cf.writerow([k[i],f'{s[i]:.3f}',f'{c[i]:.3f}'])
    
'''
In [30]: np.round(c[5], 3)
Out[30]: 0.643
'''