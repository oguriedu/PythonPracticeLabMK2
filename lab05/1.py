a=input("nhập chuỗi ký tự từ bàn phím: ")
t=0
for i in a:
    if i.isnumeric():
        print(i)
        t+=1
print(f"vậy có {t} ký tự là số trong chuỗi ký tự")

Str=input('Nhập vào một chuỗi ký tự:')
print('Chuỗi ký tự vừa nhập: ',Str)
dem=0
for c in Str:
    if "0" <= c <= "9":
        dem+=1
print('Số các ký tự là số trong chuỗi đã nhập =',dem)