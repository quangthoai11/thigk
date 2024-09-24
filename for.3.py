# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:19:32 2024

@author: Admin
"""

import random


int = [random.randint(20, 30) for _ in range(random.randint(20, 30))]
float = [num**2 for num in [random.uniform(18, 99) for _ in range(random.randint(20, 30))]]

# In kết quả
print("Danh sách số nguyên ngẫu nhiên:", int)
print("Danh sách bình phương của các số thực ngẫu nhiên:", float)



