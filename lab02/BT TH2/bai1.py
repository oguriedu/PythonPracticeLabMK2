import calendar
t=int(input("Nhập tháng: "))
print('Tháng {} có {} ngày'.format(t,calendar.monthrange(2023,t)[1]))
