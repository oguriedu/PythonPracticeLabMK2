tong_le = 0
tong_chan = 0
tong = 0
import math
n = int(input('Nhập n: '))
while n<=0:
    n = int(input('Nhập lại n: '))
    break
for i in range(1,n+1):
    if i%2==0:
        tong_chan+=1/i
    elif i%2!=0:
        tong_le+=1/i
    tong+=1/math.sqrt(i)
    
    
print('s1 = ',tong_le-tong_chan)
print('s3 =',tong-1)
