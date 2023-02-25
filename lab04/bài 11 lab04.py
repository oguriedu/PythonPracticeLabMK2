import os
print ('\n MENU ĐỒ UỐNG Ở "TIỆM NHỎ CỦA TỚ" ')
while True:
    print(' _________________________ ')
    print('|    Menu chọn đồ uống    |')
    print('| [1] Cafe                |')
    print('| [2] Cam vắt             |')
    print('| [3] Nước ép cà rốt      |')
    print('| [4] Nước lọc            |')
    print('| [5] Nước dừa            |')
    print('| [0] Bấm 0 để thoát      |')
    print('|_________________________|')

    chon = int (input('chọn đồ uống mà bạn muốn: '))
    if chon == 1:
        print ('xin chờ một lát, chúng tôi sẽ phục vụ cafe cho bạn.')
    elif chon == 2:
        print ('xin chờ một lát, chúng tôi sẽ phục vụ Cam vắt cho bạn.')
    elif chon == 3:
        print ('xin chờ một lát, chúng tôi sẽ phục vụ Nước ép cà rốt cho bạn.')
    elif chon == 4:
        print ('xin chờ một lát, chúng tôi sẽ phục vụ Nước lọc cho bạn.')
    elif chon == 5:
        print ('xin chờ một lát, chúng tôi sẽ phục vụ Nước dừa cho bạn.')
    elif chon == 0:
        break
    else:
        print('chỉ chọn các số từ 1 đến 5')
    tt = input('nhấn phím bất kì để tiếp tục (bấm 0 để thoát): ')
    if tt == '0':
        break
    else:
        os.system('cls')

