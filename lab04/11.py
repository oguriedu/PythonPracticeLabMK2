import os
while True:
    print('''
    Menu đồ uống
    1.Cafe
    2.Cam vắt
    3.Nước ép cà rốt
    4.Nước lọc
    5.Nước dừa
    ''')
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
        print('Chỉ chọn những đồ uống trên')
    i=input('Bạn có muốn tiếp tục order? Nhấn 0 để dừng lại')
    os.system('cls')    
    if i=='0':
        break
