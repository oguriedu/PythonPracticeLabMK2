print('CHƯƠNG TRÌNH QUẢN LÝ THÔNG TIN SINH VIÊN')
from tabulate import tabulate
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

name = ['mã sv', 'họ tên', 'quê quán', 'năm sinh', 'điểm trung bình các năm học']
print(tabulate(ttsvien, headers=name, tablefmt='fancy_grid', showindex='always'))