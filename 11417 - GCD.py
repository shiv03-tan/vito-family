import math
while true:
	n = int(input())
	if n == 0:
		break
        g = 0
	for i in range(1,n):
		for j in range(i+1, n+1):
			g+ = math.gcd(i,j)
	print(g)
