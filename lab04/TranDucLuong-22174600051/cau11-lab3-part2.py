a=input("Nhập kiểu hình tam giác:")
n=int(input("Nhập độ dài:"))
for t in range(1,n+1):
    for i in range(1,n+1-t):
        print("",end=" ")
    for j in range(1,t+1):
        print(a, end=" ")
    print()
