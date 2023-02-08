import math
a=int(input("nhập số a : "))
b=int(input("nhập số b : "))
c=int(input("nhập số c : "))
delta=b**2-4*a*c
if delta < 0:
    print("Phương trình vô nghiệm ")
elif delta >0:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("x1 = ",x1 ,"x2 = ",x2)
else :
    print("phương trình có 2 nghiệm phân biệt x1=x2= : ",(-b)/(2*a))