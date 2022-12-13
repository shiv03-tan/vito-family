dx = [1, -1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]
TC = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = []
    for i in range(n):
        a.append(list(input()))
 
    b = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                b[i][j] = -1
            else:
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x < n and y >= 0 and y < m and a[x][y] == "*":
                        b[i][j] += 1
    if TC > 1:
        print()
    print(f"Field #{TC}:")
    TC += 1
    for i in range(n):
        for j in range(m):
            if b[i][j] == -1:
                print("*", end="")
            else:
                print(b[i][j], end="")
        print()