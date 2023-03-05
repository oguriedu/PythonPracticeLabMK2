Str = input('Nhập vào một chuỗi ký tự:')
print('Chuỗi kí tự vừa nhập:',Str)
dem = 0
for c in Str:
    if '0' <= c <= '9':
        dem += 1
print('các số ký tự là số trong chuỗi đã nhập =',dem)
