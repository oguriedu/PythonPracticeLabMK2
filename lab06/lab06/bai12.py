nhap=input("bạn muốn làm gì? D: gửi tiền , W:rút tiền: ")
while True :
    if nhap=="D" or nhap =="W":
            break
    if nhap!="D" or nhap!="W":
        nhap=input("mời bạn nhập lại D: gửi tiền , W:rút tiền: ")
a=()
tong_tien=0
while True:
    if nhap=="D":
        tien=int(input("mời nhập số tiền cần gửi: "))
        tong_tien+=tien
        a=list(a)
        a.append("D"+" "+str(tong_tien))
        a=tuple(a)
    if nhap=="W":
        rut=int(input("mời nhập số tiền cần rút: "))
        tong_tien-=rut
        a=list(a)
        a.append("W"+" "+str(rut))
        a=tuple(a)
    tiep=int(input("bạn có muốn tiếp tục? 1:có"))
    if tiep!=1:
        break
    else:
         nhap=input("bạn muốn làm gì? D: gửi tiền , W:rút tiền: ")
for i in a:
    print(f"lịch sử giao dịch là: {i} ")

print(f"số tiền có trong tài khoản {tong_tien}")
    