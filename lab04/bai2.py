import math
a=0
b=0
c=0
cc=(-0.1)
cb=(-0.1)
ca=(-0.1)
i=1
while round(a-ca,4)!=0.0001:
    ca=a
    if i%2==0:
        a+=-(1/i)
    else:
        a=a+(1/i)
    i+=1
i=1
print(round(a,2))
while round(b-cb,4)!=0.0001:
    cb=b
    b=b+(1/(i*(i+1)))
    i+=1
i=1
print(round(b,2))

while round(c-cc,4)!=0.0001:
    cc=c
    c+=(1/(math.sqrt(i)))
    print(c)
    i+=1
print(round(c,2))

