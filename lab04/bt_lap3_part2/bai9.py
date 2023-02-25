s=0
s2=0
s3=0
n=int(input('Nhập giá trị n:'))
if n < 0:
    print('Không thỏa mãn yc đầu bài, mời bạn nhập lại!')
else:
    for i in range(1,n+1):
            s+=i**2
    print('Giá trị của dãy là:',s)

    for i in range(1,2*n+2,2):
            s2+=i**3
    print('Giá trị của dãy là:',s2)

    for i in range(2,2*n,2):
            s3+=i**4
    print('Giá trị của dãy là:',s3)