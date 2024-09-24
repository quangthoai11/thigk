# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:28:28 2024

@author: Admin
"""

n = int(input("Nhập vào số chẵn dương n để tính(2 + 4 + 6 + ... + n) "))
s = 0
while n <= 0 and n % 2 != 0:
    n = int(input("Nhập lại n là số chẵn dương: "))
for i in range (2, n + 1, 2):
   s += i
print("Kết quả là: ",s)