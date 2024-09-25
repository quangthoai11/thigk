# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:21:26 2024

@author: Admin
"""

danhsach=[]
for x in range (1,490):
    for y in range (1,140):
        for z in range (1,109):
            if 2*x + 7*y +9*z ==979:
                danhsach+=[(x,y,z)]
for i in danhsach:
    print("Bộ nghiệm" , i)