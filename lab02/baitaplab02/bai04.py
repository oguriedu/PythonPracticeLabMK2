Ia=int(input('Nhập vào 1 số nguyên: '))
if a<100:
    print(0)
else:
    b=(a%1000)//100
    print('Chữ số hàng trăm của số {} là {}'.format(a,b))