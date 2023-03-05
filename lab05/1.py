x = input('Nhập 1 chuỗi kí tự: ')
print('chuỗi vừa nhập là: ',x)
dem = 0
for i in x:
    if '0'<=i<='9':
        dem += 1
print('số các kí tự số là: ',dem)
