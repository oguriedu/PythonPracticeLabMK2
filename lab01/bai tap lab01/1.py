infor = {
    "masv": "",
    'hoten':'',
    'quequan':"",
    'namsinh': '',
    "điểm_tb": ''
}
print("nhập mã sinh viên")
infor['masv'] = int(input())
print("nhập họ tên sinh viên")
infor['hoten'] = input()
print("nhập quê quán")
infor['quequan'] = input()
print("nhập năm sinh")
infor['namsinh'] = int(input())
print("nhập điểm tb")
infor['điểm_tb'] = float(input())
print("mã sinh viên: ",infor['masv'])
print("họ tên sinh viên: ",infor['hoten'])
print("quê quán: ",infor['quequan'])
print("năm sinh: ",infor['namsinh'])
print("điểm tb: ",infor['điểm_tb'])