#bài 6
str=input('Nhập chuỗi')
Hex=''
for i in str:
    if '0'<=i<='9' or 'A'<=i<='F' or 'a'<=i<='f':
        Hex+=i
    else:
        continue
Hexupper=Hex.upper()
Code={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
Decimal=0
pos=len(Hexupper)-1
for i in Hexupper:
    if i.isnumeric():
        Decimal+=int(i)*(16**pos)
    else:
        Decimal+=Code[i]*(16**pos)
    pos-=1
print('Chuỗi sau khi loại bỏ hết kí tự không thuộc HEX là:',Hex)
print('Chuỗi sau khi chuyển từ hex sang số thập phân là: ',Decimal)