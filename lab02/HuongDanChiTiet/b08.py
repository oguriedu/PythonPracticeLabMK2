print('Chương trình trình phân loại sinh viên. ')
print('Nhập điểm sinh viên,', end='')
loai = input("điểm:")
if loai == 'A':
    print("Xếp loại xuất sắc.")
elif loai == 'B':
    print("Xếp loại Giỏi.")
elif loai == 'C':
    print("Xếp loại Khá.")
elif loai == 'D':
    print("Xếp loại Trung bình.")
elif loai == 'E':
    print("Xếp loại Yếu.")
elif loai == 'F':
    print("Xếp loại Kém.")
else:
    print("Nhập sai xin mời nhập lại điểm!")