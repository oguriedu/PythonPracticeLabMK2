n = int(input("nhập số n: "))
while n<=0:
    n = int(input("nhập số dương: "))
# phần a
S1 = 0
for i in range(1, n+1):
    S1 = S1 + i
print("tổng giá trị là: ",S1)
# phần b
S2 = 0
for i in range(1,2*n+1,2):
    S2 = S2 + i
print("tổng giá trị S2 là: ",S2)
# phần c
S3 = 0
for i in range(2,2*n,2):
    S3 = S3 + i
print("tổng giá trị là: ",S3)
