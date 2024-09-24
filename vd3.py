# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:34:47 2024

@author: Admin
"""

n = int(input("Nhập vào một số nguyên dương n: "))
dict = {i: i**3 for i in range(1, n+1)}
print(dict)