import math 
print("pt:ax2 + bx + c = 0 (a khác 0)")
a = int(input("nhập hệ số a: "))
b = int(input("nhập hệ số b: "))
while True:
    if a == 0 :
        print("Một trong hai hệ số a, b phải khác 0: ")
        a = int(input("Mời nhập lại số a: "))
    else:
        break
c = int(input("nhập hệ số c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1= x2= ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1= ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x1= ", (-(b) - math.sqrt(delta))/(2*a) )