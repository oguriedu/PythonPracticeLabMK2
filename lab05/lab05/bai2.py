nhap=input("moi nhap chuoi ")
khong=0
khong_so=0
for i in nhap:
    kiem_tra=i.isascii()
    so=i.isnumeric()
    if kiem_tra==True:
        khong+=1
    if so==False:
        khong_so+=1
print("co",khong,"khong phai tieng anh")
print("co",khong_so,"khong phai so")
