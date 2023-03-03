Str=input('Nhập vào một chuỗi ký tự:')
print('Chuỗi ký tự vừa nhập: ',Str)
dem=0
dem2=0
for c in Str:
    if "0" <= c <= "9":
        dem+=1
for c in Str:
    if "a" <= c <= "z" or "A" <= c <= "Z":
        dem2+=1

print('Số các ký tự không phải là tiếng anh trong chuỗi đã nhập =',dem)
print('Số các ký tự không phải là chữ số trong chuỗi đã nhập = ',dem2)