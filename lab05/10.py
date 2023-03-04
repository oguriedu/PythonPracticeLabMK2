a=str(input("nhập chuỗi nhị phân: "))
sum=0
m=len(a)-1
for i in a:
    if int(i) ==1:
        sum+=2**m
    if int(i)!=1 or int(i)!=0:
        print("bạn nhập sai chuỗi nhị phân")
    m-=1
print(sum)