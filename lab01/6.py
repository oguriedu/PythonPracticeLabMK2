hieu_dthe=220
cddd=2.7
cong_suat=hieu_dthe*cddd/1000
giay=int(input("Nhập thời gian sử dụng bóng đèn(giây):"))
gio=giay/3600
tien_dien=cong_suat*gio*7000
print("Thời gian sử dụng bóng đèn(giây) là ", giay,"giây")
print("Đổi giây ra giờ: ",giay,"giây =",gio,"giờ")
print("Tiền điện phải trả với giá tiền điện 7000đ/kWh là:",tien_dien,"đồng")