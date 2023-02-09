loai_xe=int(input("Cho biết loại xe là 4/7 ?"))
so_km = float(input("Nhập số km chạy = ")) 
time_cho=float(input("Cho biết thời gian chờ (phút chờ) = ")) 
tien_cuoc = float(0)
tien_di_chuyen = float(0)
if time_cho >=5:
    tien_cho=(time_cho-5)*0.8 
else:
    tien_cho=0
if loai_xe == 4:
    if so_km <=0.8:
        tien_di_chuyen = 11000
    elif so_km <=20:
        tien_di_chuyen = 11000+(20-so_km)*12100 
    else:
        tien_di_chuyen= 11000+(20-0.8)*12100+(so_km-20)*10000
    tien_cuoc= tien_cho+tien_di_chuyen
    print("Cước phí xe tacxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
#----------------------------------------------------------------------
if loai_xe == 7:
    if so_km <=0.8:
        tien_cuoc=tien_cho + 13000
    elif so_km <=30:
        tien_cuoc=tien_cho + 13000+(30-so_km)*14100
    else:
        tien_cuoc = tien_cho + 13000 +(30-0.8)*14100+(so_km-30)*12000
    print("Cước phí xe tacxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)
