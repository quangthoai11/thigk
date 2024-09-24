# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:09:59 2024

@author: Admin
"""
import math

# Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# Tính căn bậc hai của n và làm tròn xuống thành số nguyên
sqrt_n = int(math.sqrt(n))

# Kiểm tra xem bình phương của căn bậc hai có bằng n không
if sqrt_n * sqrt_n == n:
    print(n, "là số chính phương")
else:
    print(n, "không phải là số chính phương")