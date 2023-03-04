a=input("Nhập chuỗi: ")
b=0
c=0
for i in a:
    kiem_tra=i.isascii()
    so=i.isnumeric()
    if kiem_tra==True:
        b+=1
    if so==False:
        c+=1
print("Có",b,"không phải tiếng anh")
print("Có",c,"không phải số")
