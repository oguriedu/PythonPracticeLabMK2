import math
n=int(input("Nhập số n là số nguyên dương:"))
while n<0:
    n=int(input("Nhập sai, n phải là số nguyên dương:"))
#tinh S4
S4=0
i=1
while i<=n:
    S4 += math.pow(i,2)
    i+=1
#Tinh S5
S5=0
i=1
while i<=n*2+1:
    S5+=i**3
    i+=2
#Tinh S6
S6=0
i=1
while i<=2*n:
    S6+=i**4
    i+=2
print("S4=",S4)
print("S5=",S5)
print("S6=",S6)