gui=[]
rut=[]
while True:
    print('1.Gửi tiền')
    print('2.Rút tiền')
    print('3.Số tiền thực')
    print('4.Thoát chươg trình')
    chon=int(input('Chọn chức năng: '))
    if chon==1:
        a=int(input('D :'))
        gui.append(a)
        print(f'Bạn đã gửi {a} đồng vào tài khoản ')
    elif chon==2:
        b=int(input('W :'))
        if sum(gui)<b:
            print('Không đủ tiền trong tài khoản để rút')
        else:
            rut.append(b)
            print(f'Bạn đã rút {b} đồng từ tài khoản ')        
    elif chon==3:
        print(f'Số tiền thực trong tài khoản: {sum(gui)-sum(rut)} đồng')      
    else:
        break

        