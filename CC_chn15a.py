
for _ in range(int(input())):
    n,k=map(int,input().split())
    lis=list(map(int,input().split()))
    c=0
    for i in lis:
        if (i+k)%7==0:
            c+=1
    print(c)
