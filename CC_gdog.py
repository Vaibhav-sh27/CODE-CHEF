for _ in range(int(input())):
    n,k=map(int,input().split(' '))
    c=0
    for i in range(1,k+1):
        if n%i>c:
            c=n%i
    print(c)