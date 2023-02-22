a = float(input('Nhập a:'))
b = float(input('Nhập b:'))
c = float(input('Nhập c:'))
if a == 0:
    print('Phương trình không tồn tại đỉnh')
else:
    denta = b*b - 4*a*c
    x = -b/2*a
    y = -denta/(4*a)
    print('đỉnh của phương trình là (%0.2f,%0.2f)'%(x,y))