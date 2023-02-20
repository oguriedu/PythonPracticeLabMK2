#tính giá trị biểu thức
n=int(input("nhập số nguyên dương n= "))
tongS6=0
while n<=0:
    print("hãy nhập số n thỏa mãn")
    n=int(input("nhập số nguyên dương n= "))
for i in range(1,n+1):
    i=(2*i)**4
    tongS6=tongS6+i
print("giá trị của tổng S6 = ",tongS6)