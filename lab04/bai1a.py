#Tính giá trị của biểu thức
tong=0
i=1
n=int(input("Nhap  n : "))
while n<=0:
    print("Nhap lai gia tri : ")
    n=int(input())
for i in range(1,n+1):
    tong+=i**2
print("Tong s4 la : ",tong)