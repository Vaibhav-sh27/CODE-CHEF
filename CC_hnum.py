for _ in range(int(input())):
    n=int(input())
    s=0
    for i in str(n):
        s+=int(i)
    if n%s==0:
        print('Yes')
    else:
        print('No')