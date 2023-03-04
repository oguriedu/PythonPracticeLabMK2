nhap=input("moi nhap chuoi: ")
so=" "
for i in nhap:
    kiem_tra=i.isnumeric()
    if kiem_tra==True:
        so+=str(i)
uoc_nguyen=0
for k in range(1,int(so)):
    uoc=int(so)%k
    if uoc==0:
        uoc_nguyen+=k
        tim=int(so)/k
if uoc_nguyen==int(so):
        print(so,"la so hoan hao")
else:
     print(so,"khong phai la so hoan hao")

