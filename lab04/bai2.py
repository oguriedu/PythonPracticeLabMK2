import math
n = int(input("nhập n :"))
while n<=0:
    n = int(input("nhập lại n :"))
#------------------------------------------
# ý a:
s1=0
a=1
while a!=(n+1):
    s1+=(((-1)**(a+1))*(1/a))
    a+=1
print("giá trị S1 =",s1)
#------------------------------------------
# ý b:
s2=0
a=1
while a!=(n+1):
    j=(1/a)*(1/a+1)
    s2+=j
    a+=1
print("giá trị S2 =",s2)
#-------------------------------------------
# ý c:
s3=0
a=1
while a!=(n+1):
    s3+=(1/math.sqrt(a+1))
    a+=1
print("giá trị S3 =",s3)