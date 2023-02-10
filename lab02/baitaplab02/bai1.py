import calendar #lấy dữ liệu từ thư viện lịch
x= int(input("nhập năm:"))
t=int(input("Nhập tháng: "))
print('Tháng {} có {} ngày'.format(t,calendar.monthrange(x,t)[1])) #"{}" thay giá trị lần lượt các biến trong format