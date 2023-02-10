import math
x=int(input("Nhập số x: "))
bieu_thuc=(-x+math.sqrt(x**2+4))/(math.pow(x,4)**1/7)
print(round(bieu_thuc,2))