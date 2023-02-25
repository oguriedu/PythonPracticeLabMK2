n=int(input('Nhập giá trị n:'))
sum=0
while n:
    sum+=n%10
    n=int(n/10)
print('Tổng là:',sum)