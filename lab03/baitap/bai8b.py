n=int(input("moi nhap n: "))
if n<=0:
    print("moi ban nhap lai")
tong=0
for i in range(0,n+1):
    tong+=2*i+1
    if i == 2 * n + 1:
        break
print(tong)
