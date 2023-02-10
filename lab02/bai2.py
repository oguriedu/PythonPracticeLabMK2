#
import math
def giaiptb2(a,b,c):
    if(a==0):
        if b==0:
            print("Phương trình vô nghiệm")
        else:
            print("Phương trình có một nghiệm: x = ",(-c/b))
        return
    delta = b*b-4*a*c
    if delta > 0:
        x1= float((-b+math.sqrt(delta))/(2*a))
        x2=float((-b-math.sqrt(delta))/(2*a))
        print("Phương trình có 2 nghiệm là: x1 = ",x1,"và x2 = ",x2)
    elif delta==0:
        x=-b/(2*a)
        print("Phương trình có nghiệm là : x1 = x2 = ",x)
    else:
        print("Phương trình vô nghiệm")        
a=float(input("a = "))
b=float(input("b = "))               
c=float(input("c = "))
giaiptb2(a,b,c)
