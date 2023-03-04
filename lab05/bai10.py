#
a=str(input("nhập chuỗi nhị phân : "))
kq=0
b=len(a)-1
for i in a:
    if int(i) ==1:
        kq+=2**b
    if int(i)!=1 or int(i)!=0:
        print("bạn nhập sai chuỗi nhị phân")
    b-=1
print(kq)