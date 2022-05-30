for _ in range(int(input())):
    x,m=map(int,input().split(' '))
    a=[]
    x=list(str(x))
    x=list(map(int,x))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    for i in x:
        a.append((i**m)%10)
    a=list(map(str,a))
    a=a[::-1]
    if int(''.join(a))%7==0:
        print('YES')
    else:
        print('NO')
