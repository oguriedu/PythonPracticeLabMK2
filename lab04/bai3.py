import math
x=float(input("nhập x: "))
h=float(0)
i=0
while round(1-h-math.cos(x),4)!=0:
    v=float((-1)**i)*(x**(2*(i+1)))/((float(math.factorial(2*(i+1)))))
    h+=float(v)
    i+=1
    print(i)
print(1-h)