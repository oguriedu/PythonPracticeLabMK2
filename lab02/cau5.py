months = ["January", "February", "March", "April", "May", "June",\
    "July", "August", "September", "October", "November", "December"]
thang=int(input('Nhập vào tháng trong năm [1-12] :'))
if 0<thang<13:
    print(f'Tháng {thang} tương ứng với {months[thang-1]}')
else:
    print('B nhập không hợp lệ.')