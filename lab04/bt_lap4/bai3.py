import math


n=int(input('Nhập giá trị của n:'))
cos_x=1
for i in range(1,n+1):
    cos_x+=(-1)**i*(i**(2*i))/math.factorial(2*i)
print('Gía trị của biểu thức %0.4f'%cos_x)
        

