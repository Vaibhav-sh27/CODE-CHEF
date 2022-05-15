t=int(input())
while (t>0):
    lst=list(map(int,input().split(' ')))
    if(lst.count(1)>lst.count(0)):
        print("YES")
    else:
        print("NO")
    t-=1