sum=0
i=0
n=int(input('Nhập giá trị n:'))
for i in range(1,n+1):
    sum+= 1 /(i*(i+1))
print('Giá trị của dãy là:',sum)
