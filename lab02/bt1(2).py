a = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
b = int(input('Nhập tháng cần xem: '))
c = a.get(b)
print('Tháng',b,'có',c,'ngày')