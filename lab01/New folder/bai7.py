a, b, c = map(float,input("Nhập giá trị của a b c: ").split())
x = -b/2*a
y = a*x**2+b*x+c
print("Đỉnh của phương trình bậc 2 là: %0.2f"%x, '%0.2f'%y)