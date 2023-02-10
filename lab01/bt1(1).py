#Nhập thông tin sinh viên
msv = input('Nhập mã sinh viên: ')
ten = input('Nhập họ tên sinh viên: ')
que = input('Nhập quê quán sinh viên: ')
nam_sinh = int(input('Nhập năm sinh của sinh viên: '))
dtb = float(input('Nhập điểm trung bình các năm học: '))

#Xuất ra thông tin vừa nhập
print('{:20}{:20}{:20}{:20}{:>5}'.format('Mã sinh viên','Họ và tên','Quê quán','Năm sinh','Điểm trung bình môn'))
print('{:20}{:20}{:1}{:21}{:>20}'.format(msv,ten,que,nam_sinh,dtb))
