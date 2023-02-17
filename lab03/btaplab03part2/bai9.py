sum=0
n=int(input('Nhập giá trị n:'))
if n < 0:
    print('Bạn đã nhạp sai , hãy nhập lại!')
else:
    for i in range(1,n+1):
        sum+=i**2
print('Giá trị của dãy là:',sum)

for i in range(1,n+1,2):
    sum+=(2*i+1)**3
print('Giá trị của dãy là:',sum)

for i in range(-2,n+1,2):
    sum += (2*n)**4
print('Giá trị của dãy là:',sum)
