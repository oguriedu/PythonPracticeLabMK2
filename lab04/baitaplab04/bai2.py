n= int(input('nhập n:'))
import math
s1 =0
s2=0
s3=0
while n>0:
    s1=s1+(1/n)-(1/(n+1))
    n=n-1
    break
print('sum =',s1)

while n>=0:
    s2+=(1/n) + (1/(n*(n+1)) )
    n=n+1
    break
print(f'sum2 = {s2}')
while n>1:
    s3=s3+1/math.sqrt(n)
    n=n+1
    break
print(f'sum3={s3}')