n=input('Nhập chuỗi kí tự:')
dem = 0
for i in n:
    if i.isalnum() == False:
        print(i)
        dem+=1
print('Số kí tự không phải là số và chữ là:',len(i))