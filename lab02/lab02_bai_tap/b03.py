days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = int(input("Nhập ngày từ 1 đến 7: "))
if day in [1, 2, 3, 4, 5, 6, 7]:
    print("Ngày nhập tương ứng với:", days[day - 1])
else:
    print("Nhập sai giá trị.")

