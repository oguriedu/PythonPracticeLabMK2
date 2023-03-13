date=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
thu=int(input('Nhập vào thứ trong tuần [1-7] :'))
if 0<thu<8:
    print(f'Ngày {thu} tương ứng với {date[thu-1]}')
else:
    print('Bạn nhập không hợp lệ .')
