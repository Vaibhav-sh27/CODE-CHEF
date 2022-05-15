n=int(input())
lst=list(map(int,input().split(' ')))
e=0
o=0
for i in lst:
    if i%2==0:
        e+=1
    else:
        o+=1
if e>o:
    print('READY FOR BATTLE')
else:
    print('NOT READY')