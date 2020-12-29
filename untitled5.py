# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:50:00 2020

@author: ASUS_PEPE
"""

def mf(str):
    print("To jest moja funkcja = ",str)
   
if __name__=='__main__':
    mf("test")
    
import numpy as np
import matplotlib.pyplot as plt
import csv

k = np.arange(0,370,10)
s = np.sin(np.deg2rad(k))

with open ('plik2.csv','w',newline='') as f:
    cf = csv.writer(f,delimiter=';')
    for i in range(len(k)):
        cf.writerow([k[i],s[i]])

s=np.deg2rad(k)
sin=np.sin(s)
cos=np.cos(s)
plt.plot(k,sin)
plt.plot(k,cos)
plt.show