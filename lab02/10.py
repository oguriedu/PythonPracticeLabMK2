while True:
    start=int(input('Nhập giờ bắt đầu: '))
    end=int(input('Nhập giờ kết thúc: '))
    if 0<=start<5 or 0<=end<=5 or start>=22 or end>22:
        print('Sân đã đóng cửa')
    elif end>start:
        print('Đặt lại giờ')
    else:
        break
gio=end-start
if 11<=start<15 and 11<end<=15:
    if gio<=3:
        tien_thue=100000*gio*0.9
    else:
        tien_thue=100000*3*0.9+100000*(gio-3)*0.9*0.75
else:
    if gio<=3:
        tien_thue=100000*gio
    else:
        tien_thue=100000*3+100000*(gio-3)*0.75
print('Tiền khách thuê sân phải trả là: {:,} Đồng'.format(int(tien_thue)))