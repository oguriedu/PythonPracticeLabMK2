logged_in = False
while logged_in == False:
    login_ID = input('Nhập mã ID: ')

    if login_ID != "k16":
        print('Nhập sai mã ID')
    else:
        login_Password = input('Nhập mật khẩu: ')
        if login_Password == "khdl2023":
            print('Xin chào !')
            logged_in = True
        else:
            print('Bạn đã nhập sai Password!')
