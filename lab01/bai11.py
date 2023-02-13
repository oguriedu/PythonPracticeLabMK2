n = int(input('Nhập số lần tung xúc sắc: '))

p = 1 - (5**n)/(6**n)
result = p**3
print(
    f'Xác suất khi tung {n:d} lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 : {result:.2f}')
