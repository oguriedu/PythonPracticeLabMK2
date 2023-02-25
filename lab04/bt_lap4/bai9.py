n=int(input('Nhập giá trị:'))
s=0
while n:
    s+=n%10
    n=int(n/10)
print('Tổng là:',s)
