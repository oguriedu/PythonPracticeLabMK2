'''Viết chương trình nhập giờ bắt đầu, giờ kết thúc
in ra số tiền khách thuê sân tập'''
while True:
    print("5 giờ <=giờ bắt đầu <= giờ kết thúc <= 22 giờ")
    gio_bd=int(input("Nhập giờ bắt đầu:"))
    gio_kt=int(input("Nhập giờ kết thúc:"))
    if 5<=gio_bd<=gio_kt<=8:
        so_gio=gio_kt-gio_bd
        print("Số tiền khách thuê sân tập phải trả từ",gio_bd,"giờ đến",gio_kt,"giờ là:",so_gio*100000)
    
    if 8<=gio_bd<=gio_kt<=11 or 15<=gio_bd<=gio_kt<=22 :
        so_gio=gio_kt-gio_bd
        print("Số tiền khách thuê sân tập phải trả từ",gio_bd,"giờ đến",gio_kt,"giờ là:",so_gio*100000*(1-25/100))
    else:
        if 11<=gio_bd<=gio_kt<=15:
            so_gio=gio_kt-gio_bd
            print("Số tiền khách thuê sân tập phải trả từ",gio_bd,"giờ đến",gio_kt,"giờ là:",so_gio*100000*(1-35/100))



        