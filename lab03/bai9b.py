#tính giá trị biểu thức 
n=int(input("nhập số nguyên dương n = "))
tongS5=0
while n<0:
    print("hãy nhập số hợp lệ ")
    n=int(input("nhập số nguyên dương n = "))
for i in range(0,n+1):
    i=(2*i+1)**3
    tongS5=tongS5+i
print("giá trị của tổng S5 = ",tongS5)