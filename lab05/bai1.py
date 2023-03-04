Str=input('Nhập vào một chuỗi ký tự:')
print('Chuỗi ký tự vừa nhập: ',Str)
dem=0
for c in Str:
    if "0" <= c <= "9":
        dem+=1
print('Số các ký tự là số trong chuỗi đã nhập =',dem)
