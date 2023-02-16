print('CHƯƠNG TRÌNH QUẢN LÝ THÔNG TIN SINH VIÊN')
ttsvien = []

while True:
    masv = input('mã sv: ')
    hoten = input('họ tên: ')
    quequan = input('quê quán: ')
    namsinh = input('năm sinh: ')
    diemtb = input('điểm tb các năm học: ')
    ttsvien.append([masv, hoten, quequan, namsinh, diemtb])
    tt = input("bạn có muốn tiếp tục thêm? (1: có)")
    if tt != '1':
        print('đã hoàn thành!')
        break
print(ttsvien)