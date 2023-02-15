import math
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
delta=math.pow(b,2)-4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    print("Phương trình có nghiệm kép x1 = x2 =",-b/(2*a))
else:
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1 = ", (-b + math.sqrt(delta)/(2*a)))
    print("x2 = ", (-b - math.sqrt(delta)/(2*a)))