def isprime(num):
    for n in range(2,num):
        if num%n==0:
            return False
    return True
for _ in range(int(input())):
    n=int(input())
    c=0
    for i in range(2,n//2+1):
        if isprime(i):
            if isprime(n-i):
                print(i,n-i)
                c=1
                break
            
    if c==0:
        print(-1,-1)