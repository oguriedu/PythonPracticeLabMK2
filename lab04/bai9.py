n = input('nhập số n:')
try:
    temp = 0
    for i in n:
        temp += int(i)
    print('tổng các chữ só của số vừa nhập là',temp)
except:
    print('số vừa nhập không hợp lệ!')

