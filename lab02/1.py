month = int(input("Nhập vào một tháng (từ 1 đến 12): "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    print("Tháng", month, "có 31 ngày")
elif month in [4, 6, 9, 11]:
    print("Tháng", month, "có 30 ngày")
elif month in [2]:
    print("Tháng", month, "có 28 hoặc 29 ngày")
else:
    print(month,'không phải tháng hợp lệ')