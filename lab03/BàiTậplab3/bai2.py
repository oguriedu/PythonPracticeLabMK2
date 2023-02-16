# Số hoàn hảo nhỏ hơn n
n=int(input("Nhập n: "))
tong=0
print("Các số hoàn hảo nhỏ hơn",n,"là:")
for i in range(1,n+1):
    n-=1
    tong*=0
    for j in range(0,n-1):
        j+=1
        if n%j==0:
            tong+=j
    if tong==n :
        print(tong,end=",")   
    if n==1:
        break
        