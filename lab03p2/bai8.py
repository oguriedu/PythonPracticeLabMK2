#a
n=int(input('nhập n:'))
tong=0
if n<0:
    print('nhập sai,mời bạn nhập lại!')
else:
    for i in range(0,n+1):
        tong+=i*(i+1)/2
        print('tổng là:',tong)
#b
n=int(input('nhập n:'))
tong=0
if n<=0:
    print('nhập sai, mời bạn nhập lại!')
else:
    for i in range(1,n+2):
        tong+=(2*i)+1
        print('tổng là:',tong)
#c
n=int(input('nhập n:'))
tong=0
if n<=0:
    print('nhập sai,mời bạn nhập lại!')
else:
    for i in range(2,n+2):
        tong+=(i*2)+1
        print('tổng là:',tong)