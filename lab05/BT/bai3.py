n=-1
while (n<=0):
    n = int(input("nhập n>0 :"))
#chuyển từ hệ số 10 sang hệ số 2
x = n
kq=""
while(n>0):
    kq=str(n%2)+kq
    print("n%2=",n%2)
    n = n//2
    print("n=",n)
print("kết quả =",kq)