print("Nhập số dương n:")
n=int(input())
for i in range(1,n):
            tong=0
            if(n%i==0):
                tong += i
if(tong == n):
    print("Là số hoàn hảo")
else:
    print("Không phải là số hoàn hảo")