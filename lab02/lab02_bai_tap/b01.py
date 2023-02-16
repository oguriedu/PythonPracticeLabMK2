month = int(input("Nhập ngày trong tháng (1-12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31 ngày")
elif month == 2:
    print("28/29 ngày")
else:
    print("30 ngày")
