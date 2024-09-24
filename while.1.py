# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:12:54 2024

@author: Admin
"""

so = float(input("Nhập vào số [-99; 99] : "))

while so < -99 or so > 99:
    so = float(input("Không đúng,vui lòng nhập lại : "))
print("Giá trị thỏa điều kiện")