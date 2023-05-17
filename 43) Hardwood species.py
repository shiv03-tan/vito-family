# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:57:19 2023

@author: wwf
"""

import sys

test_case = int(input())
input()
while test_case > 0:
    counter = 0
    hardwood = {}

    while True:
        try:
            tree = input().strip()
            if tree == "":
                break
            counter += 1
            hardwood[tree] = hardwood.get(tree, 0) + 1
        except EOFError:
            break

    for tree, count in sorted(hardwood.items()):
        percentage = (count / counter) * 100
        print(f"{tree} {percentage:.4f}")

    test_case -= 1
    if test_case > 0:
        print()
