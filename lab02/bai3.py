def welcome():
    a = input('Nhập vào thứ (1->7) trong tuần:')
    return a
def thu():
    a = welcome()
    if a == '1':
        print('sunday')
    elif a == '2':
        print('monday')
    elif a == '3':
        print('Tuesday')
    elif a == '4':
        print('wednesday')
    elif a == '5':
        print('thursday')
    elif a == '6':
        print('friday')
    elif a == '7':
        print('saturday')
    else:
        thu()
thu()


