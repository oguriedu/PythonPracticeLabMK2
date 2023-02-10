diem=float(input("Nhập điểm TK: "))
if diem<4:
    print("Loại Kém")
elif diem<5:
    print("Loại Yếu")
elif diem<7:
    print("Loại TB")
elif diem<9:
    print("Loại Khá")
else:
    print("Loại Giỏi")