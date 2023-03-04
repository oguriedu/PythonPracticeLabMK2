str = input('Nhập vào một chuỗi ký tự: ')
print('Chuỗi ký tự vừa nhập là: ',str)
dem = 0
dem2 = 0
for a in str:
    if "0" <= a <= "9":
        dem+=1
for a in str:
    if "a" <= a <= "z" or "A" <= a <= "Z":
        dem2+=1

print('Số các ký tự không phải là tiếng anh trong chuỗi đã nhập =',dem)
print('Số các ký tự không phải là chữ số trong chuỗi đã nhập = ',dem2)
