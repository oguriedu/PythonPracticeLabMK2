print("Menu:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

n = int(input("Chọn thức uống theo số trên menu: "))

if n == 1:
    print("Bạn đã chọn Cafe.")
elif n == 2:
    print("Bạn đã chọn Cam vắt.")
elif n == 3:
    print("Bạn đã chọn Nước ép cà rốt.")
elif n == 4:
    print("Bạn đã chọn Nước lọc.")
elif n == 5:
    print("Bạn đã chọn Nước dừa.")
else:
    print("Số bạn chọn không hợp lệ. Vui lòng thử lại.")