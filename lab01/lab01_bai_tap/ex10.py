import math

a = float(input('Nhập vận tốc của xe: '))

t = (a**4)/(math.log(5, 4))
print(f'Thời gian: {t:.2f}')
