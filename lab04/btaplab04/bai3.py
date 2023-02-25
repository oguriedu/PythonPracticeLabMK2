import math
n=int(input('Nhập giá trị n:'))
cosx=1
for i in range(1,n+1):
    cosx+=(-1)**i*(i**(2*i))/math.factorial(2*i)
print('Gía trị của biểu thức là:',cosx)