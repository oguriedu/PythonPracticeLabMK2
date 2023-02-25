import os
print('   CHƯƠNG TRÌNH GỌI ĐỒ UỐNG  ')
while True:
    #hiển thị menu chọn chức năng:
    print('|_______________________________|')
    print('|      Menu chọn đồ uống        | ')
    print('|[1]:-------- Cafe -------------|')
    print('|[2]:------- Cam vắt -----------|')
    print('|[3]:------- Nước ép cà rốt ----|')
    print('|[4]:-------- Nước lọc ---------|')
    print('|[5]:------- Nước dừa ----------|')
    print('|_______________________________|')
    print('|[0]: bấm chọn số 0 để thoát khỏi chương trình ')

    menu=int(input('chọn chức năng cần thực hiện : '))
    if menu==1:
        print('bạn chọn đồ uống là Cafe')
    elif menu==2:
        print('bạn chọn đồ uống là Cam vắt ')
    elif menu==3:
        print('bạn chọn đồ uống là Nước ép cà rốt ')
    elif menu==4:
        print('bạn chọn đồ uống là Nước lọc ')
    elif menu==5:
        print('bạn chọn đồ uống là Nước dừa ')
    elif menu==0:
        break
    else:
        print('chỉ chọn các mục chức năng có sẵn ')
    #break
    tt=input('hãy nhấn phím bất kì để tiếp tục chương trình, hoặc bấm chọn số 0 để thoát ')
    if tt=="0":
        break
    else: os.system('cls')