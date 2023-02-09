month=['January','February','March','April','May','June','July','August','September','October','November','December']
while True:
    a=int(input('Nhập tháng: '))
    if 0<a<13:
        break
    print('Không hợp lệ vui lòng nhập lại!')
print(f"{a}: {month[a-1]}")