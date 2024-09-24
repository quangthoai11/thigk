# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:43:54 2024

@author: Admin
"""

N = int(input("Nhập vào một số nguyên dương N: "))
while N < 0:
      N = int(input("Nhập lại một số nguyên dương N: "))
print(f"Các ước số của {N} là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)
