# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:32:54 2024

@author: Admin
"""

so = float(input("Nhập vào số [-89.9; 88.8] : "))

while so < -89.9 or so > 88.8:
    so = float(input("Không đúng, vui lòng nhập lại: "))
print("Số bạn nhập thỏa điều kiện")