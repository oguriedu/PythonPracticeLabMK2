#tính giá trị của tổng S2
n=int(input("nhập n = "))
tongS2=0
while n<0:
    print("nhập lại cho hợp lệ ")
    n=int(input("nhập n = "))
for i in range(0,n+1):
    i=i*2+1
    tongS2=tongS2+i
print("giá trị của tổng S2 = ",tongS2)