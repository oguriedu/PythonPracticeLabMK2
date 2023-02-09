import calendar
month = int (input('nhập tháng: '))
def month_test(month):
    if month < 1 or month > 12:
        print ('nhập sai, mời nhập lại!!')
    else:
        if month in (1, 3, 5, 7, 8, 10, 12):
            print ('tháng', month, 'có 31 ngày')
        elif month == 2:
            year = int (input('nhập năm: '))
            if calendar.isleap ( year ) == True:
                print ('tháng 2 có 29 ngày')
            else:
                print ('tháng 2 có 28 ngày')
        else:
            print ('tháng', month, 'có 30 ngày')
    return
print (month_test(month))