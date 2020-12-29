# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 11:11:38 2020

@author: lab
"""

a = float(input('a='))
b = float(input('b='))

try:
    c=a/b

    print('a/b=',str(c))
except:
    print('b==0')