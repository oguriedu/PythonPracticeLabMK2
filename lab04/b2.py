import math

n = int(input('Nhập n: '))
while n<=0:
    n = int(input('Nhập n > 0: '))
s1=0
m=1
while m!=(n+1):
    s1+=(((-1)**(m+1))*(1/m))
    m+=1
print('S1=',s1)
s2=0
m=1
while m!=(n+1):
    j=(1/m)*(1/m+1)
    s2+=j
    m+=1
print('S2=',s2)
s3=0
m=1
while m!=(n+1):
    s3+=(1/math.sqrt(m+1))
    m+=1
print('S3=',s3)
