import os
print('\n CHƯƠNG TRÌNH GỌI ĐỒ UỐNG.')
while True:
    #hiển thị menu đồ uống
    print('_____________________________________________')
    print('|            Menu chọn đồ uống              |')
    print('|[1] Chọn Cafe                              |')
    print('|[2] Chọn Cam Vắt                           |')
    print('|[3] Chọn Nước Ép Cà Rốt                    |')
    print('|[4] Chọn Nước Lọc                          |')
    print('|[5] Chọn Nước Dừa                          |')
    print('|[0] Bấm số 0 để thoát                      |')
    print('|___________________________________________|')

    chon=int(input("Chọn đồ quốc bạn cần: "))
    if chon ==1:
        print("Bạn chọn cafe.")
    elif chon==2:
        print("Bạn chọn cam vắt.")
    elif chon==3:
        print("Bạn chọn nước ép cà rốt.")
    elif chon==4:
        print("Bạn chọn nước lọc.")
    elif chon==5:
        print("Bạn chọn nước dừa.")
    elif chon==0:
        break
    else:
        print("Chỉ chọn từ 1-5")
        #break
    tt=input("Nhập phím bất kì tiếp tục , bấm số 0 để thoát.")
    if tt=='0':
        break
    else: os.system('cls')