# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:57:19 2023

@author: wwf
"""
T = int(input())

for i in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    step1 = x1 + ((x1 + y1) * (1 + x1 + y1) // 2)
    step2 = x2 + ((x2 + y2) * (1 + x2 + y2) // 2)

    if step1 > step2:
        print(f"Case {i}: {step1 - step2}")
    else:
        print(f"Case {i}: {step2 - step1}")