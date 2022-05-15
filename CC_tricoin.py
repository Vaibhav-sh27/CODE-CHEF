for i in range(int(input())):
    n=int(input())
    c=0
    for j in range(1,n+1):
        if ((j*(j+1))/2)<=n:
                c+=1
        else:
            break
    print(c)