print('\n\n\t\t============MENU============')
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")
print('\n\t\t============END============')
# Người dùng nhập lựa chọn
print('Hãy nhập lựa chọn của bạn  (1-->4):', end='')
luachon = int(input())
# Cấu trúc if elif else
if luachon == 1:
    print('Bạn đã lựa chọn thể loại phim tình cảm\n')
elif luachon == 2:
    print('Bạn đã lựa chọn thể loại phim kinh dị\n')
elif luachon == 3:
    print('Bạn đã lựa chọn thể loại phim hoạt hình\n')
elif luachon == 4:
    print('Bạn đã lựa chọn thể loại phim khoa hoc viễn tưởng\n')
else:
    print('Lựa chọn không hợp lệ. Xin vui lòng kiểm tra lại')
