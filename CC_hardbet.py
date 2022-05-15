t=int(input())
while (t>0):
    lst=list(map(int,input().split(' ')))
    if(min(lst)==lst[0]):
        print("Draw")
    elif(min(lst)==lst[1]):
        print("Bob")
    elif(min(lst)==lst[2]):
        print("Alice")
    t-=1