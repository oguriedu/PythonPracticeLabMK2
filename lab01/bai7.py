#Chương trình tìm đỉnh của một phương trình bậc hai
import math
a=float(input("nhập hệ số a: "))
b=float(input("nhập hệ số b: "))
c=float(input("nhập hệ số c: "))
if a==0 or b!=0:
    print("phương trình không có đỉnh")
else:
    delta=b**2-4*a*c
    if delta>=0:
        print("phương trình có đỉnh là :",-b/2*a)
        
            