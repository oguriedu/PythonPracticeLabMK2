import os
print('\n CHƯƠNG TRÌNH GỌI ĐỒ UỐNG ')
while True:
    print(' ____________________________________________')
    print('|             Menu đồ uống:                   |')
    print('| [1] Cafe                                    |')
    print('| [2] Cam vắt                                 |')
    print('| [3] Nước ép cà rốt                          |')
    print('| [4] Nước lọc                                |')
    print('| [5] Nước dừa                                |')
    print('| [0] Không chọn loại nào,thoát chương trình  |')
    print('|_____________________________________________|')
    chon = int(input('Chọn đồ uống: '))
    if chon==1:
        print('Bạn đã chọn Cafe')
    elif chon==2:
        print('Bạn đã chọn cam vắt')
    elif chon == 3:
        print('Bạn đã chọn nước ép cà rốt')
    elif chon == 4:
        print('Bạn đã chọn nước lọc')
    elif chon==5:
        print('Bạn đã chọn nước dừa')

    else:
        print('Bạn đã không chọn loại nào và thoát chương trình  ')
    tt=input('Bạn có muốn tiếp tục gọi đồ ? 0:không;số bất kì:có')
    if tt=='0':
        break
    else:
        os.system('cls')