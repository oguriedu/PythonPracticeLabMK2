import math
x=float(input("Nhap so: "))
a=(-x+math.sqrt(x**2+4))/(pow(x**4+1, 1/7))
a=round(a,2)
print("Kết quả là : ",a)