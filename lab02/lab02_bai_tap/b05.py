months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
month = int(input("Nhập tháng từ 1 đến 12: "))
if month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    print("Tháng tương ứng:", months[month - 1])
else:
    print("Nhập sai giá trị.")
