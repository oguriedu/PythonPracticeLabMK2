#viết chương trình:
thang= int(input("Nhập tháng mà bạn cần xem ngày: "))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print("tháng đã nhập có 31 ngày")
elif thang == 2:
    nam= int(input("nhập năm : "))
    if (nam % 4 == 0 and nam % 100 != 0):
        print("Tháng 2 có 29 ngày vì năm nhuận")
    else:
        print("Tháng 2 có 28 ngày vì năm không nhuận")
else:
    print("Tháng đã nhập có 30 ngày")
