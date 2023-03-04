Str=input('Nhập vào một chuỗi ký tự:')
a=0
b=0
for i in Str:
    if "0" <= i <= "9":
        a+=1
for i in Str:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        b+=1
print('Số các ký tự không phải là tiếng anh :',a)
print('Số các ký tự không phải là chữ số :',b)