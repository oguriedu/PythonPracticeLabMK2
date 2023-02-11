def welcome():
    a = input('Nhập vào tháng (1->12) trong năm:')
    return a
def thang():
    a = welcome()
    if a == '1':
        print('January')
    elif a == '2':
        print('February')
    elif a == '3':
        print('March')
    elif a == '4':
        print('April')
    elif a == '5':
        print('May')
    elif a == '6':
        print('June')
    elif a == '7':
        print('July')
    elif a == '8':
        print('August')
    elif a == '9':
        print('September')
    elif a == '10':
        print('October')
    elif a == '11':
        print('November')
    elif a == '12':
        print('December')
    else:
        print('Mời nhập lại!!!')
        thang()

thang()