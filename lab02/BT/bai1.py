import calendar
a=int(input("nhap thang "))
print("tháng {} có {} ngày".format(a,(calendar.monthrange(2023,a)[1])))