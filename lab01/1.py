ma_sv=int(input("Nhập mã sinh viên: "))
ho_ten=input("Nhập họ tên sinh viên:")
que_quan=input("Nhập quê quán sinh viên:")
nam_sinh=int(input("Nhập năm sinh sinh viên:"))
diem_tb=[]
for i in range(0,5):
    diem_tb.append(float(input("Nhập điểm trung bình 5 năm học:")))
print("--------------------------")
print("Mã sinh viên:",ma_sv)
print("Họ tên sinh viên:",ho_ten)
print("Quê quán sinh viên:",que_quan)
print("Năm sinh sinh viên:",nam_sinh)
print("Điểm trung bình các năm học:",diem_tb)
