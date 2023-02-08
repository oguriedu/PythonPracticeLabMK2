giobatdau=float(input("Nhập thời gian bắt đầu : "))
gioketthuc=float(input("Nhập thời gian kết thúc : "))
while True:
    if giobatdau<5 and gioketthuc>22:
        print("Thời gian bắt đầu phải lớn hơn 5 giờ sáng và thời gian kết thúc phải trước 22 giờ tối \n (trong đó: thời gian kết thúc phải lớn hơn thời gian bắt đầu) ")
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
