import math
i=0
sum=0
n=int(input('Nhập giá trị n:'))
for i in range(0,n+1):
    sum+=math.sqrt(i)
print('Giá trị của dãy là:',sum)