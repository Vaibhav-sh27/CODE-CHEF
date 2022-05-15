for i in range(int(input())):
    x,y,Xr,Yr,D=map(int,input().split(' '))
    if min(x/Xr,y/Yr)>=D:
        print('YES')
    else:
        print('NO')