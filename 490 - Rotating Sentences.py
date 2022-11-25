
list=[]
count=0
maxLength=0
while True:
    try:
        n=input()
        list.append(n)
        count+=1
        if maxLength<len(n):
            maxLength=len(n)
    
    except EOFError:
        for i in range(0,maxLength):
            j=count-1
            while j>=0:
                if len(list[j])>i:
                    print(list[j][i],end="")
                else:
                    print(" ",end="")
                j=j-1
            print()
        break;
        