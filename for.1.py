# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:49:43 2024

@author: Admin
"""


n = int(input("Nhập số nguyên dương n: "))
giai_thua = 1
for i in range(1, n+1):
    giai_thua *= i
print("Giai thừa của", n, "là:", giai_thua)


