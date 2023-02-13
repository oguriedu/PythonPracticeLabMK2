print("Nhập các số :", end='')
a, b, c = map(float, input('=').split(','))
max = a
if max < b:
    max = b
if max < c:
    max = c
print('Số lớn nhất trong 3 số %0.2f , %0.2f, %0.2f ' %
      (a, b, c), 'là %0.2f' % max)
