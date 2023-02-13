#1KWh = 1000(W). 3600(s) = 3600000(J)
u = 220
i = 2.7
t = float(input('Nhập thời gian sử dụng bóng đèn là: '))
A = u*i*t
result = (A/3600000)*7000
print(f'Số tiền phải trả: {result}')
