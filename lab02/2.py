import math
a=float(input("nhập vào hệ số a: "))
b=float(input("nhập vào hệ số b: "))
while True:
    if a == 0 and b == 0:
        print("Một trong hai hệ số a, b phải khác 0: ")
        a = float(input("Mời nhập lại số a: "))
        b = float(input("Mời nhập lại số b: "))
    else:
        break
c=float(input("nhập vào hệ số c: "))
delta=b**2-4*a*c


if delta >0:
    print('pt có 2 nghiệm',(-(b) + math.sqrt(delta))/(2*a),(-(b) - math.sqrt(delta))/(2*a))
elif delta==0:
    print('pt có 1 nghiệm kép','x1=x2','=',-b/2*a)
else:
    print('pt vô nghiệm')