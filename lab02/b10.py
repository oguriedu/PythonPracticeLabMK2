print("Chương trình tính thu nhập (lương ròng) của nhân viên. ")
luong = float(input("Nhập lương của nhân viên: "))
if luong <= 7000000:
    thue_suat = 10
    tien_thue = luong*0.1
elif luong <= 15000000:
    thue_suat = 20
    tien_thue = luong*0.2
else:
    thue_suat = 30
    tien_thue = luong*0.3
luong_rong = luong - tien_thue
print("Lương nhân viên: %0.2f" % luong, 'VNĐ/tháng')
print("Thuế suất là %d" % thue_suat, "%")
print("Tiền lương thực nhận là: %0.2f" % luong_rong, 'VNĐ/tháng')
    