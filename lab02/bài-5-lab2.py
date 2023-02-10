b=['January','February','March','April','May','June','July','August','September','October','November','December']
while True:
    a=int(input('nhập tháng trong năm mà bạn muốn: '))
    if 0<a<13: 
        print(a,':',b[a-1])
        break