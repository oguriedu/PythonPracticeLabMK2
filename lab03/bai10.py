a= int(input("nhập số "))
t=[]
for k in range(2,a+1):
    for i in range(2,k+1):
        if(k==i):
            t+=[k]
            break
        if (k%i==0):
            break
tt=[]
h=a
for i in t:
    m=0
    while a%i ==0:
        a=a/i
        m+=1
        if a==1:
            break
    tt+=[m]
l=''
x=0
for i in t:
    if tt[x]==0:
        x+=1
        continue
    ll=f"{i}^{tt[x]}"
    l+=ll+"*"
    x+=1
print(l.rstrip("*"))