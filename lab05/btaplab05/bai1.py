n=input('Nhập chuỗi kí tự:')
dem = 0
for i in n:
    if i>="0" and i<="9":
        dem += 1
print('Số các kí tự là số trong string là:',dem)