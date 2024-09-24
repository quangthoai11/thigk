# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:01:42 2024

@author: Admin
"""

n = int(input("Nhập vào số nguyên dương n để tính(1 + 2 + 3 + ... + n) "))
s = 0
while n <= 0:
    n = int(input("Nhập lại n là số nguyên dương: "))
for i in range (1, n + 1):
    s += i
print("Kết quả là: ",s)