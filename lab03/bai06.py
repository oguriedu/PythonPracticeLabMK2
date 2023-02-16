# Tổng bậc 3 của n số nguyên đầu tiên
n=int(input("Nhập n:"))
tong=0
for i in range(1,n+1):
    tong+=i*i*i
print(tong)