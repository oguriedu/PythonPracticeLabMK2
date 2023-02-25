import math
n = int(input('Nhập n: '))
while n<=0:
    n = int(input('Nhập sai . Nhập lại n > 0: '))
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
print('tổng s1 là %0.3f'%s1)
print('tổng s2 là %0.3f'%s2)
print('tổng s3 là %0.3f'%s3)

