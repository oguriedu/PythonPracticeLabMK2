print('Nhập a1,b1,c1:')
a1 = float(input('a1='))
b1 = float(input('b1='))
c1 = float(input('c1='))
print('Nhập a2,b2,c2:')
a2 = float(input('a1='))
b2 = float(input('b1='))
c2 = float(input('c1='))
# tính định thức d,dx,dy
d = a1*b2-a2*b1
dx = c1*b2-c2*b1
dy = a1*c2-a2*c1
if d != 0:
    print('Phương trình có nghiệm duy nhất x=%0.2f và y=%0.2f'
          % ((dx/d), (dy/d)))
else:
    if dy == 0 and dx == 0:
        print("Vô định ")
    else:
        print("Vô nghiệm.")
