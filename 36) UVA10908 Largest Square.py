# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:57:19 2023

@author: wwf
"""
testCaseNum = int(input())

for _ in range(testCaseNum):
    height, width, squareLocationNum = map(int, input().split())
    print(height, width, squareLocationNum)

    square = []
    for _ in range(height):
        square.append(input())

    for _ in range(squareLocationNum):
        row, column = map(int, input().split())
        largestSide_half = 0

        center = square[row][column]

        largestHeight = min(row, height - row - 1)
        largestWidth = min(column, width - column - 1)
        largestPossibleSide_half = min(largestHeight, largestWidth)

        isSquare = True
        for k in range(1, largestPossibleSide_half + 1):
            isSquare = all(square[m][n] == center for m in range(row - k, row + k + 1) for n in range(column - k, column + k + 1))
            if isSquare:
                largestSide_half += 1
            else:
                break

        print(largestSide_half * 2 + 1)
