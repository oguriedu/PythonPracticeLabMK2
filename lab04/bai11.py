print("Menu:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

drink_choice = input("Chọn thức uống theo số trên menu: ")

if drink_choice == "1":
    print("Bạn đã chọn Cafe.")
elif drink_choice == "2":
    print("Bạn đã chọn Cam vắt.")
elif drink_choice == "3":
    print("Bạn đã chọn Nước ép cà rốt.")
elif drink_choice == "4":
    print("Bạn đã chọn Nước lọc.")
elif drink_choice == "5":
    print("Bạn đã chọn Nước dừa.")
else:
    print("Số bạn chọn không hợp lệ. Vui lòng thử lại.")
