#tính giá trị biểu thức
import math
n= int(input("nhập số nguyên dương n = "))
tongS3=0
while n<=0:
    print("hãy nhập lại số n thỏa mãn đề bài ")
    n=int(input("nhập số n nguyên dương = "))
for i in range(2,n+1):
    tongS3=tongS3+1/(math.sqrt(i))
print("giá trị của biểu thức = ",tongS3)