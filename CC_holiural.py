for _ in range(int(input())):
    n,k=map(int,input().split(' '))
    d=list(map(int,input().split(' ')))
    r=list(map(int,input().split(' ')))
    c=[d[i]*k+r[i] for i in range(n)]
    print(min(c))
