import math
n = int(input('Nhập n: '))
while n<=0:
    n = int(input('Nhập n > 0: '))
#a
s1=0
a=1
while a!=(n+1):
    s1+=(((-1)**(a+1))*(1/a))
    a+=1
print('S1 = ',s1)
#b
s2=0
a=1
while a!=(n+1):
    j=(1/a)*(1/a+1)
    s2+=j
    a+=1
print('S2=',s2)
#c
s3=0
a=1
while a!=(n+1):
    s3+=(1/math.sqrt(a+1))
    a+=1
print('S3=',s3)