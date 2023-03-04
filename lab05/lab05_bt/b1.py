str=input('nhập chuỗi kí tự :')
print('chuỗi kí tự vừa nhập là :',str)
dem=0
for i in str:
    if "0" <= i <= "9":
        dem+=1
print('số các kí tự là số trong chuỗi là:',dem)