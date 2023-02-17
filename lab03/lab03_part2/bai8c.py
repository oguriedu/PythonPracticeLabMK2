s=0
n=int(input("Nhập n số nguyên dương: "))
while n<0:
    n=int(input("Nhập n số nguyên dương: "))
for i in range(1,n+1):
    s+=i*2
print("Tổng của S3 là ",s)