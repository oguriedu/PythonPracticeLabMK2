n=int(input("Nhập n:"))
if n<=0:
    print("Nhập lại:")
tong=0
for i in range(0,n+1):
    tong+=2*i
print(tong)