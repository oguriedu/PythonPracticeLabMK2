#Tính tổng
tong=0
i=1
n=int(input("Nhap n : "))
while n<=0:
    print("Nhap lai gia tri : ")
    n=int(input())
for i in range(1,n+1):
    tong+=(1/i)*(1/i+1)
print("Tong s4 la : ",tong)