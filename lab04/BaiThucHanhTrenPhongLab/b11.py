print("Menu:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")
menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]
while True:
    n = input("Nhap lua chon cua ban: ")
    if n.isnumeric() and int(n) in [1, 2, 3, 4, 5]:
        print(f"Lua chon: {menu[int(n)-1]}")
    elif len(n) == 0:
        break
    else:
        print("Khong co trong danh sach")
print("Ket thuc")
