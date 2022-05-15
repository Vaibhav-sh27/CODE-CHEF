for _ in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split(' ')))
    e=0
    o=0
    for i in range(n):
        if i%2==0:
            e+=lst[i]
        else:
            o+=lst[i]
    if e>o:
        print(e)
    else:
        print(o)
