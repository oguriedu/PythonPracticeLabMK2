thu = int (input('nhập thứ: '))
def xet_thu (thu):
    if thu < 1 or thu > 7:
        print ('không hợp lệ, mời nhập lại!!')
    else:
        if thu == 1:
            print ('Sunday')
        elif thu == 2:
            print ('Monday')
        elif thu == 3:
            print ('Tuesday')
        elif thu == 4:
            print ('Wednesday')
        elif thu == 5:
            print ('Thursday')
        elif thu == 6:
            print ('Friday')
        else:
            print ('Saturday')
    return
print (xet_thu(thu))