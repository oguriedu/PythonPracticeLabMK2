str = input('Nhập vào một chuỗi ký tự: ')
print('Chuỗi ký tự vừa nhập là: ',str)
dem = 0
for a in str:
    if "0" <= a <= "9":
        dem+=1
print('Số các ký tự là số trong chuỗi đã nhập =',dem)
