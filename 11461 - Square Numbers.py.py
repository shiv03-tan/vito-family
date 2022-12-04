p  = [ 0  for  i  in  range ( 100001 )]

#mark the perfect square number
for  i  in  range ( 317 ):      #316*316=99856
    p[i*i] = 1

#Statistics i contains several complete square numbers
for  i  in  range ( 1 , 100001 ):
    p[i] += p[i-1]

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    
    print(p[b] - p[a-1])