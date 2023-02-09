while True:
    gbd=float(input("Nhập thời gian bắt đầu : "))
    gkt=float(input("Nhập thời gian kết thúc : "))
    if gbd<5 and gkt>22:
        print("Thời gian không hợp lệ:")
    else:
        tg_thue=gkt-gbd
        if tg_thue>3:
            print("Số tiền thuê sân là : ",tg_thue*75000)
        if 11<=gbd<=15 and 11<=gkt<=15:
            print("Số tiền thuê sân là : ",tg_thue*90000)
        elif 0<tg_thue<=3:
            print("Số tiền thuê sân là : ", tg_thue*100000)