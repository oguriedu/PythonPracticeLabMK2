number = int(input("Nhập một số nguyên có 3 chữ số: "))

if number >= 100:
    # chia 100 lấy hàng 100
    # chia lấy dư cho 10 lấy số hàng trăm
    print("Số hàng trăm là:", number // 100 % 10)
else:
    print("Số hàng trăm là: 0")
