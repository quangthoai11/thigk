# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:15:11 2024

@author: Admin
"""

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

S = x
mau_so = 1

for i in range(2, n+1):
  mau_so += i
  S += x**i / mau_so

print("Tổng S(n) =", S)