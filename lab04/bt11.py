while True:
    print("______________________________")
    print("|MENU CHỌN ĐỒ UỐNG           |")
    print("|1: Cafe                     |")
    print("|2: Cam vắt                  |")
    print("|3: Nước ép cà rốt           |")
    print("|4: Nước lọc                 |")
    print("|5: Nước dừa                 |")
    print("|____________________________|")
    chon=int(input("Lựa chọn:"))
    if chon==1:
        print("Bạn chọn Cafe")
    if chon==2:
        print("Bạn chọn Cam vắt")
    if chon==3:
        print("Bạn chọn Nước ép cà rốt")
    if chon==4:
        print("Bạn chọn Nước lọc")
    if chon==5:
        print("Bạn chọn Nước dừa")
        break
    else:
        kt=int(input("Nhập 1 để tiếp tục khác 1 dừng lại."))
        if kt!=1:
            break