import math
x=input("Nhập x: ")
n=int(input("Nhập n: "))
cx=1-(math.pow(x,3)/(n*(n-1)))
print("cos(",x,") = %0.4f"(cx))