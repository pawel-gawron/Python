# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:17:40 2020

@author: ASUS_PEPE
"""

Keep_going=True

while Keep_going:
        print("jaka opcje chcesz wybrac")
        print("Do wyboru X lub x")
        wybor = str(input("wybor: "))
        try:
            if wybor=="X" or wybor=="x":
                print("udalo sie")
                Keep_going=False
                print("Koniec programu")
        except:
            print(wybor)
