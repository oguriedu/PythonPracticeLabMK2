#Viết chương trình nhập vào x tính giá trị biểu t@@ -0,0 +1,4 @@
import math
x=float(input('Nhập x = '))
fx=math.log(x,4)+math.log(2,x)
print("f(x) = ",round(fx,2))
