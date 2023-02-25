def menu():
        print('1.Cafe')
        print('2.Cam vắt')
        print('3.Nước ép cà rốt')
        print('4.Nước lọc')
        print('5.Nước dừa')
        n=int(input('Mời bạn nhập mã đồ uống:'))
        if n==1:
            print('Bạn đã chọn Cafe!')
        elif n==2:
            print('Bạn đã chọn Cam vắt!')
        elif n==3:
            print('Bạn đã chọn Nước ép cà rốt!')
        elif n==4:
            print('Bạn đã chọn Nước lọc!')
        elif n==5:
            print('Bạn đã chọn Nước dừa!')
        else:
            print('Mã bạn nhập không có trong menu.Mời bạn nhâp lại!!')
print('----------------Menu----------------')
menu()