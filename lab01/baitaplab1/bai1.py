list=[]
def them_sinh_vien(list):
    while True:
        masv=int(input("nhập vào mã sinh viên: "))
        hoten=input("nhập vào họ tên sinh viên: ")
        quequan=input("quê quán là: ")
        namsinh=int(input("năm sinh là: "))
        diemtrungbinh=float(input("nhập điểm trung bình các năm:"))
        list.append({'masv':masv,'hoten':hoten,'quequan':quequan,'namsinh':namsinh,"diemtrungbinh":diemtrungbinh})
        tt=input("bạn có muốn tiếp tục khoog(1=1tt")
        if tt!='1':
            break
    return
print("thông tin sinh viên là",them_sinh_vien(list))