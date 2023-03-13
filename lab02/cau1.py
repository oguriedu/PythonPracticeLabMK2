thang=int(input('Nhập vào tháng muốn kiểm tra số ngày 1-12:'))
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print(f'Tháng {thang} có 31 ngày.')
elif thang == 2:
    print(f'Tháng {thang} có 28 or 29 ngày.')
    
elif thang in [4, 6, 9, 11]:
    print(f'Tháng {thang} có 30 ngày')
else:
    print('Bạn nhập tháng không hợp lệ')
