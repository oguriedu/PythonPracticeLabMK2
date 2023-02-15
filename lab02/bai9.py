so_kw=float(input("mời nhập số KW: "))
if so_kw>0 and so_kw<=100:
        don_gia=2000*so_kw
elif so_kw>100 and so_kw<=200:
        don_gia=2500*so_kw
else:
        don_gia=3000*so_kw
if so_kw>300:
    don_gia=5000*so_kw
print("số tiền điện là: ",don_gia)