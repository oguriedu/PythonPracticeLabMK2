Str = input('Nhập vào một chuỗi kí tự:')
print('chuỗi ký tự vừa nhập',Str)
dem = 0
for c in Str:
    if c.isalpha(): 
        continue
    elif '0' < c < '9':
        continue
    else:
        dem += 1
print('số ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi Str=',dem)

