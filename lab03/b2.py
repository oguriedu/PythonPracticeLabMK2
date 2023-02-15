n=int(input("mời nhập vào n: "))
a=0
for i in range(n+1):
    n-=1
    a*=0
    for j in range(0,n-1):
        j+=1
        if n%j==0:
            a+=j
    if a==n :
        print(a)   
    if n==1:
        break
