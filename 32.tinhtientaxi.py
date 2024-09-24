# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:01:45 2024

@author: Admin
"""

km = float(input("Nhập vào số km đi được: "))
tien_cuoc = 0
if km <= 1:
    tien_cuoc = 15000
elif km <= 5:
    tien_cuoc = 15000 + (km - 1) * 13500
else:
    tien_cuoc = 15000 + 4 * 13500 + (km - 5) * 11000
if km > 120:
    tien_cuoc *= 0.9
print(f"Tổng tiền cước taxi là: {round(tien_cuoc)}đ")



