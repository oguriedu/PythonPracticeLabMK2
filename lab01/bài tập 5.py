a1 = int (input('nhập số phần tử của vector a: '))
b1 = int (input('nhập số phần tử của vector b: '))
a = []
b = []
for i in range (a1):
    x = int (input ('nhập phần tử a thứ ' + str(i+1) + ': '))
    a.append(x)
for i in range (b1):
    y = int (input ('nhập phần tử b thứ ' + str(i+1) + ': '))
    b.append(y)
print ('vector a: ', a)
print ('vector b: ', b)
Tinh = []
for i in range(0, len(a)):
    Tinh.append(a[i] * b[i])
t = sum (Tinh)
print ('tích vô hướng = ', t)
