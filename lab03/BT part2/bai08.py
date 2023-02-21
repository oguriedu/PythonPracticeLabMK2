#phần a
n=int(input("nhập n : "))
tong=0
if n<=0:
    print("vui lòng nhập lại !!!!")
else:
    for i in range(0,n+1):
        tong+=i*(i+1)/2
    print("tổng là : ",tong)
#phần b
n=int(input("nhập n : "))
tong=1
if n<=0:
    print("vui lòng nhập lại!!!")
else:
    for i in range(1,n+2):
        tong+=(2*i)+1
    print("tổng là :",tong)