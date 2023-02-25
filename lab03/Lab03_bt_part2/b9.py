n=int(input("Nhập số nguyên dương: "))
if n<=0:
     print("Nhập sai, số n phải lớn hơn 0. Nhập lại")

     n=int(input("Nhập số nguyên dương: "))
s1=0
s2=0
s3=0
for i in range(1,n+1):
    k1=i**2
    k2=(2*i*1)**3
    k3=(2*i)**4
    s1+=k1
    s2+=k2
    s3+=k3
print('Tổng của n số nguyên dương 1 là:',s1)
print('Tổng của n số nguyên dương 2 là:',s2)
print('Tổng của n số nguyên dương 3 là:',s3)
