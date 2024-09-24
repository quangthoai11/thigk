# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 14:28:34 2024

@author: Admin
"""

n = int(input("Nhập vào số lẻ dương n để tính(1 * 2 * 3 * ... * n) "))
s = 1
while n <= 0 or n % 2 ==0 :
    n = int(input("Nhập lại n là số nguyên dương: "))
for i in range (1, n + 1):
   s = s * i
print("Kết quả là: ",s)