import math
n = int(input('Nhập n: '))
while n<=0:
    n = int(input('Nhập n > 0: '))
s1=0
s2=0
s3=0
a=1
while a!=(n+1):
    s1+=(((-1)**(a+1))*(1/a))
    j=(1/a)*(1/a+1)
    s2+=j
    s3+=(1/math.sqrt(a+1))
    a+=1
print('S1=',s1)
print('S2=',s2)
print('S3=',s3)
    