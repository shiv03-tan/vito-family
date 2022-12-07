
while True:
    try:
        x = int(input())
        A = list(map(int, input().strip().split()))
        ans = 0
        n = len(A) - 1
        for i in range(n):
            ans += A[i] * (n-i) * pow(x, n-1-i)
        print(int(ans))
    except:
        break