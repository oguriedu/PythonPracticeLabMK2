str=input('nhập vào 1 chuỗi ký tự :')
print('chuỗi ký tự vừa nhập là:',str)
dem=0
for c in str:
    if "0" <= c <= "9":
        dem+=1
        
print('số các ký tự là số trong đã nhập =',dem)