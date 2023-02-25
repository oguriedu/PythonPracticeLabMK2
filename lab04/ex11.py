menu = {1: "Cafe",2: "Cam vắt",3: "Nước ép cà rốt",4: "Nước lọc",5: "Nước dừa"}
while True:
    # Hiển thị menu
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value}")
    pick = input("Vui lòng chọn đồ uống (hoặc nhập 'q' để thoát): ")
    if pick == "q":
        break
    elif int(pick) in menu:
        drink = menu[int(pick)]
        print(f"Bạn đã chọn {drink}")
    else:
        print("Vui lòng chọn một đồ uống từ menu.")