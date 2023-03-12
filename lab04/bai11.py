def back():
	print('{:?^99}\n'.format(' Bạn có muốn tiếp tục order '))
	print('{:^99}'.format('1.Tiếp tục        Any key.Thoát'))
	z = input('Entry your choose:')
	if z == '1':
		return 1

while True:
    print('{:*^70}'.format(' MENU '))
    print('''
    1.Cafe
    2.Cam vắt
    3.Nước ép cà rốt
    4.Nước lọc
    5.Nước dừa''')
    n = input('entry your chose:')
    if n == '1':
        print('Bạn đã chọn cafe!')
        a = back()
        if a != 1:
            break
    elif n == '2':
        print('bạn đã chọn cam ép!')
        b = back()
        if b != 1:
            break
    elif n =='3':
        print('bạn chọn nước ép cà rốt!')
        c = back()
        if c != 1:
            break
    elif n == '4':
        print('bạn chọn nước lọc!')
        d = back()
        if d != 1:
            break
    elif n == '5':
        print('bạn chọn nước dừa!')
        e = back()
        if e != 1:
            break
    else:
        print('mời bạn nhập lại!!!')
        continue
