ngay=int(input('Nhập ngày: '))
month=int(input('Nhập tháng: '))

if month in [1, 3, 5, 7, 8, 10, 12]:
    day=list(range(1,32))
elif month in [4, 6, 9, 11]:
    day=list(range(1,31))
elif month in [2]:
    day=list(range(1,29))
if ngay==day[-1]:
    if month==12:
        print('Ngày tiếp theo của ngày {} tháng {} là ngày 1 tháng 1'.format(ngay,month))
    else:
        print('Ngày tiếp theo của ngày {} tháng {} là ngày 1 tháng {}'.format(ngay,month,month+1))
else:
    print('Ngày tiếp theo của ngày {} tháng {} là ngày {} tháng {}'.format(ngay,month,ngay+1,month))

