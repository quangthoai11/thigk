# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:01:38 2024

@author: Admin
"""

danhsach=[]
max=0
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y +9*z ==979:
                sum = x+y+z
                if sum > max :
                    max=sum
                    danhsach=[(x,y,z)]

print(f"{danhsach} với bộ nghiệm (x+y+z)={max}")