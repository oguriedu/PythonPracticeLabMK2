'''Viết chương trình giải phương trình bậc 2'''
import math 
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
# Giải phương trình bậc 2: ax^2 +bx + c=0
def giai_ptbac2(a,b,c):
    if a==0:
        if b==0:
            print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có nghiệm: x=",(-c/b))
        return

delta=b**2-4*a*c
if delta >0:
    x1=float((-b+math.sqrt(delta))/(2*a))
    x2=float((-b-math.sqrt(delta))/(2*a))
    print("Phương trình có 2 nghiệm là: x1 =",x1,"và x2=",x2)
elif delta==0:
    x12=-b/2*a
    print("Phương trình có nghiệm kép: x1=x2=",x12)
else:
    print("Phương trình vô nghiệm!")
# Nhập các hệ số