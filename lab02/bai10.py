#chương trình tính tiền thuê sân bóng đá
import math
gio_bat_dau=int(input("nhập giờ bắt đâu vào sân bóng :"))
gio_ket_thuc=int(input("nhập giờ kết thúc : "))
gio_tren_san=int(gio_ket_thuc-gio_bat_dau)

if gio_tren_san<=0:
    print("bạn chưa thuê sân tập")
for i in int(gio_tren_san):
    if i<3:
        print("giá tiền phải trả là : ",i*100000,"đồng")
    else:
        print("giá tiền phải trả là : ",(100000*i)-0.25*(100000*i),"đồng")
if 11<=gio_bat_dau<=15 and gio_ket_thuc<=22:
    for i in int(gio_tren_san):
        print("giá tiền phải trả là : ",i*100000-(i*10000*0.1),"đồng")
 

