n=int(input('nhập số nguyên dương N:'))
a=2
b=print('thừa số nguyên tố')
for i in range(2,n+1):
    if n%a==0:
        print(b,a,end=' ')
        n=n/a
    else:
        a+=1