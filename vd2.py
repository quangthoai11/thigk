# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:28:01 2024

@author: Admin
"""

numbers=(num for num in range(2020,3839) if num % 2 ==0)
number=(n for n in numbers if n % 9 ==0)
for danhsach in number:
    print(danhsach , end='\t')