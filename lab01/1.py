masv = input("nhập mã sinh viên ")
tên = input("nhập tên học sinh: ")
quequan = input("nhập quê quán: ")
namsinh = input("nhập năm sinh: ")

# 
diem= []

# lấy điểm
for _ in range(0, 5):
    diem.append(float(input("nhập điểm: ")))

# xuất ra
print("masv: ", masv)
print("tên: ", tên)
print("quequan: ", quequan)
print("namsinh: ", namsinh)
print("diem: ", diem)