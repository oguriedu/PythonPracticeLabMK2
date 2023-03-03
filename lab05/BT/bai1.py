s = input('Nhập 1 chuỗi kí tự: ')
print('chuỗi vừa nhập là: ',s)
dem = 0
for c in s:
    if '0'<=c<='9':
        dem += 1
print('số các kí tự số là: ',dem)