#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 22:17:01 2022

@author: sonyaridesia
"""
def ordinal():
    print("\nOrdinal Number")
    print("\nketik 0 untuk menghentikan program")
    while True:
        num = int(input("Masukan sebuah angka: "))
        if num in [10, 11, 12, 13]:
            print("(", num, "'th'", ")")
        else:
            ka = num % 10
            if ka == 1:
                print("(", num, "'st", ")")
            elif ka == 2:
                print("(", num, "'nd'", ")")
            elif ka == 3:
                print("(", num, "'rd'", ")")
            else:
                print("(", num, "'th'", ")")
        if num == 0:
            print("Terima kasih sudah menggunakan program")
            print("Sonya Ridesia - 064002200007")
            break
a = ordinal()
print(a)