n= int(input('nhập n:'))
m=n
a=n
s4 = 0
s5 = 1
s6 = 0
while True:
    if n<=0:
        print('bạn nhập sai ,nhập lại')
        n=int(input('nhập lại  n'))
    while n>0:
        s4=s4+n**2
        n=n-1
    print(f'tổng s4 là {s4}')
    while m>0:
        s5=s5+(2*m+1)**3
        m=m-1
    print(f'tổng s5 là :{s5}')
    while a>0:
        s6=s6+(2*a)**4
        a=a-1
    print(f'tổng s6 là: {s6}')
    break