n=int(input('nhập n: '))
def a(x):
    i=1; s=0
    while i<x:
        if x%i==0: s=s+i
        i+=1
    if x==s: print(x)
    return 
c=1
while c<n:
    a(c)
    c+=1