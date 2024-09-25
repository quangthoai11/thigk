# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:52:17 2024

@author: Admin
"""

N = int(input("Nhập vào một số nguyên dương N: "))
tong = 0
while N <= 0:
    N = int(input("N phải là số nguyên dương. Nhập lại N: "))
while N > 0:
    tong += N % 10
    N //= 10
print("Tổng các chữ số là:", tong)
