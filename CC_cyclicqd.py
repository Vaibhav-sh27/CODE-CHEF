for i in range(int(input())):
    a,b,c,d=map(int,input().split(' '))
    if (a+b+c+d==360) and (a+c==180) and (b+d==180):
        print('YES')
    else:
        print('NO')