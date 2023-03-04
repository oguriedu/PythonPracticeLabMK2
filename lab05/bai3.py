n=-1
while (n<=0):
    n=int(input("nhập vào n > 0: "))
#chuyển từ hệ 10 sang nhị phân
ketqua=""
x=n
while(n>0):
    ketqua=str(n%2)+ketqua
    print("n%2= ",n%2)
    n=n//2
    print("n= ",n//2)
print("kết quả sau khi chuyển là: ",ketqua)