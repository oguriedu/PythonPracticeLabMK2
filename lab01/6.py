s=int(input("mời bạn nhập số giây"))
doi_don_vi=s/60/60
hieu_dien_the=220
cuong_do_dong_dien=2.7
cong_suat=hieu_dien_the*cuong_do_dong_dien
tien_dien=cong_suat*7000*doi_don_vi
print("tiền điện là: ",tien_dien/1000)