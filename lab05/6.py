Str=input('Nhập chuỗi')
hex=''
n =0 
for i in Str:
    if '0'<=i<='9' or 'A'<=i<='F' or 'a'<=i<='f':
        n+=i
    else:
        continue
a=hex.upper()
Code={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
sothapphan=0
pos=len(a)-1
for i in a:
    if i.isnumeric():
        sothapphan+=int(i)*(16**pos)
    else:
        sothapphan+=Code[i]*(16**pos)
    pos-=1
print('Chuỗi sau khi loại bỏ hết kí tự không thuộc HEX là:',hex)
print('Chuỗi sau khi chuyển từ hex sang số thập phân là: ',sothapphan)