import csv,os

lstsinhvien=[]
def them_sv(lstsinhvien):
    while True:
        ma_sv=int(input("Nhập mã sinh viên: "))
        hvt_sv=input("Nhập tên sinh viên: ")
        que_quan=input("Nhập quê quán: ")
        nam_sinh=input("Nhập năm sinh của sinh viên: ")
        diem_tb=float(input("Nhập điểm trung bình: "))
        tt=input("Bạn có tiếp tục nhập thêm không? (1:tiếp tục)")
        lstsinhvien.append([{'ma_sv':ma_sv,'hvt_sv':hvt_sv,'que_quan':que_quan,'nam_sinh':nam_sinh,'diem_tb':diem_tb}])
        if tt!='1':
            break
    return 
#------------
def in_ds_sinhvien(lstsinhvien):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('so_hd','ngay_hd',\
         'ho_tenkh','dia_chi','quan',\
        'dien_thoai','tong_tien_hd','tam_ung','con_lai'))
    
    for hd in lstsinhvien:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(hd['so_hd'],\
            hd['ngay_hd'], hd['ho_tenkh'],hd['dia_chi'],hd['quan'],\
        hd['dien_thoai'],hd['tong_tien_hd'],hd['tam_ung'],hd['con_lai']))

    return
while True:    
 print("1: thêm sinh viên")
 print("2: in danh sách sinh viên")
 chon=int(input('Chọn chức năng cần thực hiện: '))
 if chon ==1:
    them_sv(lstsinhvien)
 elif chon==2:
    in_ds_sinhvien(lstsinhvien)
    tt=input("Bạn có tiếp tục nhập thêm không?")
    if tt!='1':
            break
    