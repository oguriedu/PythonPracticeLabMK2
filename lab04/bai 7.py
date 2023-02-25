m=int(input('Nhập số nguyên thứ nhất: '))
n=int(input('Nhập số nguyên thứ hai: '))
t=m*n
if m<n:
    temp=m;m=n;n=temp
while m!=n:
    p=m-n
    if p>n:m=p
    else:
        m=n
        n=p
print('BCNN =',t//m)