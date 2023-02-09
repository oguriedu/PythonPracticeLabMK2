month = int (input('nhập tháng: '))
def month_test(month):
    if month < 1 or month > 12:
        print ('nhập sai, mời nhập lại!!')
    else:
        if month == 1:
            print ('January')
        elif month == 2:
            print ('February')
        elif month == 3:
            print ('March')
        elif month == 4:
            print ('April')
        elif month == 5:
            print ('May')
        elif month == 6:
            print ('June')
        elif month == 7:
            print ('July')
        elif month == 8:
            print ('August')
        elif month == 9:
            print ('September')
        elif month == 10:
            print ('October')
        elif month == 11:
            print ('November')
        else:
            print ('December')
    return
print (month_test(month))