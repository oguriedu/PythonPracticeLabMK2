import math
print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")
a = float(input("nhập hệ số a: "))
b = float(input("nhập hệ số b: "))
c = float(input("nhập hệ số c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )