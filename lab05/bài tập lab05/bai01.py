str=input('Nhập 1 chuỗi ký tự: ')
dem=0
for c in str:
    if '0'<= c <='9':
        dem+=1
print('Số các ký tự là số là:',dem)