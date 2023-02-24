# bài 1
# ý a:
n = int(input("nhập n: "))
while n<=0:
    n = int(input("nhập lại n : "))
s4=0
a=1
while n!=(n+1):
    s4+=a**2
    a+=1
print("tổng S4 = ",s4)
#---------------------------------------------
# ý b:
s5=0
a=1
while a!=(n+1):
    s5+=(2*a+1)**3
    a+=1
print("tổng S5 = ",s5)
#----------------------------------------------
# ý c:
s6=0
a=1
while a!=(n+1):
    s6+=(2*n)**4
    a+=1
print("tổng S6 = ",s6)