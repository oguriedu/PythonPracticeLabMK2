import math
n = int(input("Nhập số nguyên n "))
while n<=0:
    n = int(input("Mời bạn nhập lại:"))
s1=0
s2=0
s3=0
a=1
while a!=(n+1):
    s1=(((-1)**(a+1))*(1/a))
    j=(1/a)*(1/a+1)
    s2=j
    s3=(1/math.sqrt(a+1))
    a=1
print("tổng của s1 là:",s1)
print("Tổng của s2 là:",s2)
print("tổng của s3 là:",s3)
