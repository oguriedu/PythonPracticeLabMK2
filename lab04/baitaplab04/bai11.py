while True:
    print("______________________________")
    print("     MENU CHỌN NƯỚC UỐNG      |")
    print(" 1: Cafe                      |")
    print(" 2: Cam vắt                   |")
    print(" 3: Nước ép cà rốt            |")
    print(" 4: Nước lọc                  |")
    print(" 5: Nước dừa                  |")
    print("______________________________|")
    choice=int(input("Lựa chọn:"))
    if choice==1:
        print("Bạn chọn Cafe")
    if choice==2:
        print("Bạn chọn Cam vắt")
    if choice==3:
        print("Bạn chọn Nước ép cà rốt")
    if choice==4:
        print("Bạn chọn Nước lọc")
    if choice==5:
        print("Bạn chọn Nước dừa")
        break
    else:
        tt=int(input("Nhập 1 để tiếp tục,nhập khác 1 dừng lại."))
        if tt!=1:
            break