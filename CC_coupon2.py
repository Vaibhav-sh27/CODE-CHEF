for _ in range(int(input())):
    d,c=map(int,input().strip().split())
    a1,a2,a3=map(int,input().split(' '))
    b1,b2,b3=map(int,input().split(' '))
    cou=0
    if((a1+a2+a3)>=150):
        cou+=(a1+a2+a3)
    else:
        cou+=a1+a2+a3+d

    if((b1+b2+b3)>=150):
        cou+=b1+b2+b3
    else:
        cou+=b1+b2+b3+d

    t=(a1+a2+a3+b1+b2+b3+d+d)


    if(cou+c<t):
        print("YES")
    else:
        print("NO")