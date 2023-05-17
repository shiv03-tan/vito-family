# -*- coding: utf-8 -*-
"""
Created on Wed May 17 14:39:17 2023

@author: User
"""
n, m = map(int, input().split())
pre = [[0] * (m+1) for _ in range(n+1)]

while True:
    try:
        sx, sy, d = input().split()
        sx, sy = int(sx), int(sy)
        cmd = input()
        flag = False

        for i in cmd:
            if i == 'F':
                if d == 'N':
                    sy += 1
                elif d == 'E':
                    sx += 1
                elif d == 'W':
                    sx -= 1
                elif d == 'S':
                    sy -= 1
            elif i == 'R':
                if d == 'N':
                    d = 'E'
                elif d == 'E':
                    d = 'S'
                elif d == 'W':
                    d = 'N'
                elif d == 'S':
                    d = 'W'
            else:
                if d == 'N':
                    d = 'W'
                elif d == 'E':
                    d = 'N'
                elif d == 'W':
                    d = 'S'
                elif d == 'S':
                    d = 'E'

            if sx < 0 or sy < 0 or sx > n or sy > m:
                if d == 'N':
                    sy -= 1
                elif d == 'E':
                    sx -= 1
                elif d == 'W':
                    sx += 1
                elif d == 'S':
                    sy += 1

                if pre[sx][sy] == 1:
                    continue

                flag = True
                pre[sx][sy] = 1
                break

        if not flag:
            print(sx, sy, d)
        else:
            print(sx, sy, d, 'LOST')

    except EOFError:
        break