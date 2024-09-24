# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:42:40 2024

@author: Admin
"""

n = int(input("Nhập giá trị n: "))
s = 0

for i in range(n+1):
  s += 1 / (2*i + 1)

print("Tổng S(n) =", s)