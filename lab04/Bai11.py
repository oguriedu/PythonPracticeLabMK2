# Hiển thị menu đồ uống
print("Menu đồ uống:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước")

# Nhập vào lựa chọn từ bàn phím
while True :
     lua_chon = int(input("Chọn một đồ uống (1-4): "))
     if lua_chon >4:
        print("Vui long nhap lai")
     if lua_chon == 1:
      print("Bạn đã chọn Cafe.")
     if lua_chon == 2:
        print("Bạn đã chọn Cam vắt.")
     if lua_chon == 3:
        print("Bạn đã chọn Nước ép cà rốt.")
     if lua_chon == 4:
          print("Bạn đã chọn Nước.")
          break

      