import math
n=int(input("Nhập n (là số nguyên dương): "))
while n<=0:
    n=int(input("Mời bạn nhập lại n: "))
s4=0
s5=0
s6=0
for i in range(1,n+1):
    s4+=math.pow(i,2)
    s5+=math.pow((2*i+1),3)
    s6+=math.pow(2*i,4)
print("S4 =",int(s4),"\n","S5 =",int(s5),"\n","S6 =",int(s6),"\n")
