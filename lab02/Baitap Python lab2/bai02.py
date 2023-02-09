import math
# Nhập số a, b và kiểm tra điều kiện khác 0
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))

if a == 0:
    if b==0:
        print("phương trình không có nghiệm ")
    else:
        print("phương trình có nghiệm duy nhất là : ",-c/b)
else:
   delta = b**2-4*a*c
# Tìm nghiệm của phương trình
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )