n=int(input("Nhập n: "))
tong=0
while True:
    if n<=0:
        n=int(input("Nhập lại n: "))
    for i in range(0,n+1):
        tong+=(2*i)**4
    if i==n:
        break
print(tong)
