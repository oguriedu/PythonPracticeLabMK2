n=int(input("Nhập n: "))
tong=0
hieu=0
while True:
    if n<=0:
        n=int(input("Nhập lại n: "))
        break
    for i in range(1,n+1):
        if i%2!=0:
            tong+=1/i
        if i%2==0:
            hieu+=-1/i
    if i==n:
        break
print(tong+hieu)
