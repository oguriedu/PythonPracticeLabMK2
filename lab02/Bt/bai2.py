import math
a=float(input("Mời bạn nhập hệ số a: "))
b=float(input("Mời bạn nhập hệ số b: "))
while True:
    if a==0 and b==0:
        print("Một trong hai hệ số a, b phải khác 0: ")
        a = float(input("Mời nhập lại số a: "))
        b = float(input("Mời nhập lại số b: "))
    else:
        break
c=float(input("Mời bạn nhập hệ số c: "))
delta=b**2-4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    print("Phương trình có nghiệm kép x1 = x2 = ",-(b/(2*a)))
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ",(-(b)+math.sqrt(delta))/(2*a))
    print("x1 = ",(-(b)-math.sqrt(delta))/(2*a))