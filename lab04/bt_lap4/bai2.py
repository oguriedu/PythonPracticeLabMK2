import math

n=int(input('Nhập giá trị n:'))
s=0
s2=0
s3=0
for i in range(1,n+1):
    if i%2!=0:
        i=1/i
    else:
        i=-1/i
    s+=i
print('Gía trị của biểu thức:%0.2f'%s)
for i in range(1,n+1):
    s2=1-1/i
print('Gía trị của biểu thức:%0.2f'%s2)
for i in range(2,n+1):
    s3+=1/math.sqrt(i)
print('Gía trị của biểu thức:%0.2f'%s3)