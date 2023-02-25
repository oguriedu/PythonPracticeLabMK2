sum=0
i=0
n=int(input('Nhập giá trị n:'))
while n<=0:
    print('Bạn đã nhập sai , hãy nhập lại!')
    n=int(input('Nhập lại đi:'))
for i in range(1,n+1):
    sum+=(2*i)**4
print('Giá trị của dãy là:',sum)