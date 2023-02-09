import math
x= float(input(" nhập giá trị của X :"))
F= (-x+ math.sqrt(x**2+4))/((math.sqrt(x**4+1))**(1/7))
print(" giá trị của f là : %0.2f"%F)
