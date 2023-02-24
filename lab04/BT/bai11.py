print('MENU ĐỒ UỐNG')
print('1. Cafe')
print('2. Cam vắt')
print('3. Nước ép cà rốt')
print('4. Nước lọc')
print('5. Nước dừa')
while True:
    n = int(input('Mời bạn nhập đồ uống :'))
    if n >5:
        n = int(input('Mời bạn nhập lại : '))
    if n == 1:
        print('Bạn đã chọn Cafe')
    elif n==2:
        print('Bạn đã chọn cam vắt')
    elif n==3:
        print('Bạn đã chọn Nước ép cà rốt')
    elif n==4:
        print('Bạn đã chọn nước lọc')
    else:
        print('Bạn đã chọn nước dừa')
    tt = input('bạn có muốn tiếp tục chọn? 1:TT   #1: 0')
    if tt !='1':
        break
    