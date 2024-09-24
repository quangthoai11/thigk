# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 12:09:59 2024

@author: Admin
"""
import math

import math
n = int(input("Nhập vào số nguyên dương n: "))
if int(math.sqrt(n)) ** 2 == n:
    print(f"{n} là số chính phương")
else:
    print(f"{n} không phải là số chính phương")
