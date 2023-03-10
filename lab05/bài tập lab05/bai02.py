str=input('Nhập 1 chuỗi ký tự: ')
dem=0
for c in str:
    if c.isnumeric() or c.isalpha() :
        dem+=1
print('Số các ký tự không phải số, không phải chữ cái tiếng anh là:',len(str)-dem)