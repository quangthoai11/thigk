# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 22:01:42 2024

@author: Admin
"""

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tạo thành tam giác
if a + b > c and b + c > a and c + a > b:
    # Là tam giác
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or c == a:
        print("Tam giác cân")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Ba số đã nhập không tạo thành một tam giác")
    
    
    
    
    

