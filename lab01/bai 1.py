ma_sv=int(input('Nhập mã sinh viên: '))
hoten=input("Nhập họ tên: ")
que_quan=input("Nhập quê quán: ")
nam_sinh=int(input("Nhập năm sinh: "))
diem_tb=float(input("Nhập điểm trung bình các năm học: "))
print("Thông tin sinh viên: ")
print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format('Mã sinh viên','Họ Tên','Quê quán','Năm sinh','Điểm trung bình các năm học'))
print('{:^20}{:^20}{:^20}{:^20}{:^20}'.format(ma_sv,hoten,que_quan,nam_sinh,diem_tb))
