# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:20:23 2024

@author: Admin
"""


n = int(input("Nhập n: "))
tong = 0
for i in range(1, n+1):
    tong += (2*i + 1) / (2*i + 2)
print("Tổng S(n) =", tong)