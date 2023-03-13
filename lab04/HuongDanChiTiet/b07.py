import os
print('\n   CHƯƠNG TRÌNH TÍNH TOÁN CỘNG,TRỪ, NHÂN, CHIA.')
while True:
    # Hiển thị menu chọn chức năng
    print(' _________________________________________________')
    print("|                Menu chọn chức năng:             |")
    print("|[1] Thực hiện phép tính cộng                     |")
    print("|[2] Thực hiện phép tính trừ                      |")
    print("|[3] Thực hiện phép tính nhân                     |")
    print("|[4] Thực hiện phép tính chia.                    |")
    print("|[0] Bấm số 0 để thoát                            |")
    print('|_________________________________________________|')

    chon = int(input('Chọn chức năng cần thực hiện: '))
    if chon == 1:
        print('Bạn đã chọn phép tính cộng.')
    elif chon == 2:
        print('Bạn đã chọn phép tính trừ.')
    elif chon == 3:
        print('Bạn đã chọn phép tính nhân')
    elif chon == 4:
        print('Bạn đã chọn phép tính chia')
    elif chon == 0:
        break
    else:
        print('Chỉ chọn trong các số từ 1-4')
        # break
    tt = input('Nhấn phím bất kỳ để tiếp tục, bấm số 0 để thoát.')
    if tt == '0':
        break
    else:
        os.system('cls')
