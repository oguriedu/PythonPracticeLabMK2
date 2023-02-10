gio_bat_dau=int(input("mời nhập giờ bắt đầu: "))
gio_end=int(input("mời nhập giờ kết thúc: "))
giam_gia=0

while gio_bat_dau<5:
    gio_bat_dau=int(input("mời nhập giờ bắt đầu: "))
while gio_end>=22:
    gio_end=int(input("mời nhập lại giờ kết thúc"))
while gio_end<=gio_bat_dau:
    gio_end=int(input("giờ kết thúc phải lớn hơn giờ bắt đầu, mời nhập lại giờ kết thúc: "))
    gio_bat_dau=int(input("mời nhập lại giờ bắt đầu: "))
while gio_bat_dau<=5 and gio_end>=22 and gio_end<gio_bat_dau:
    gio_bat_dau=int(input("mời nhập lại giờ bắt đầu: "))
    gio_end=int(input("mời nhập lại giờ kết thúc: "))
thoi_gian_choi=gio_end-gio_bat_dau
if thoi_gian_choi<=3:
    thanh_tien=thoi_gian_choi*100000
elif thoi_gian_choi>3:
    thanh_tien=((thoi_gian_choi-3)*75000)+3*100000
if gio_bat_dau>=11 and gio_end<=15:
    giam_gia=10000
print("tiền sân: ",thanh_tien+giam_gia)
