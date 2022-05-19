for _ in range(int(input())):
    x,y,z=map(int,input().split(' '))
    if (x+(2*z))>=y:
        print('YES')
    else:
        print('NO')