giobatdau=float(input("Nhập thời gian bắt đầu:"))
gioketthuc=float(input("Nhập thời gian kết thúc:"))
while True:
    if giobatdau<5 and gioketthuc>22:
        print("Bạn đã nhập sai , 5 giờ <= giờ bắt đầu <= giờ kết thúc <= 22 giờ")
        giobatdau=float(input("Nhập thời gian bắt đầu : "))
        gioketthuc=float(input("Nhập thời gian kết thúc : "))
    else:
        break
tong_tg_thue=gioketthuc-giobatdau
if tong_tg_thue>3:
    print("Số tiền thuê sân là : ",tong_tg_thue*75000,' đồng')
if 11<=giobatdau<=15 and 11<=gioketthuc<=15:
     print("Số tiền thuê sân là : ",tong_tg_thue*90000,' đồng')
elif 0<tong_tg_thue<=3:
    print("Số tiền thuê sân là : ", tong_tg_thue*100000,' đồng')