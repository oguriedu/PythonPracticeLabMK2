n=int(input("nhập giá trị n: "))
tong=1
s=1
for i in range(0,n+1):
    a=(2*(n+1))/((2*n)+3)
    s*=a
    tong+=s
print("tổng là %0.3f"%tong)
