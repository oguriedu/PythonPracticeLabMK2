import math
a = float(input('Nhập hệ số a:'))
b = float(input('Nhập hệ số b:'))
while True:
    if a == 0 and b == 0:
        print('hệ số a hoặc b phải khác 0')
        a = float(input('Nhập lại số a:'))
        b = float(input('Nhập lại số b:'))
    else:
        break
c = float(input('Nhập hệ số c:'))
delta = (b**2)-(4*a*c)
if delta < 0:
    print('Phương trình vô nghiệm')
elif delta == 0:
    print('Phương trình có nghiệm kép x1=x2=',-(b/(2*a)))
else:
    print('Phương trình có hai nghiệm phân biệt:')
    print('x1 = ',(-(b) + math.sqrt(delta))/(2*a))
    print('x1 = ',(-(b) - math.sqrt(delta))/(2*a))