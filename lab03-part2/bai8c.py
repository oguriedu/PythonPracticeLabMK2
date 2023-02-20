#tính giá trị biểu thức
n=int(input("nhập số n = "))
tongS3=0
while n<=0:
    print("hãy nhập số n dương ")
    n=int(input("nhập số n = "))
for i in range(1,n+1):
    i=i*2
    tongS3=tongS3+i
print("giá trị của tổng S3 = ",tongS3)