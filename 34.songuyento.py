# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:13:44 2024

@author: Admin
"""

n = int(input("Nhập vào số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải là số nguyên dương. Nhập lại n: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố.")
            break
    else:
        print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")
