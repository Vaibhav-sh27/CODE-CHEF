for i in range(int(input())):
    n,s=map(int,input().split(' '))
    p=(n*(n+1))//2 -s
    if(p<=n and p>=1):
        print(int(p))
    else:
        print(-1)