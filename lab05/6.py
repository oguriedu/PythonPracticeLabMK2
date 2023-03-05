a=input('Nhập chuỗi :')
b=''
for i in a:
    if '0'<=i<='9' or 'A'<=i<='F' or 'a'<=i<='f':
        b+=i
    else:
        continue
d=b.upper()
c={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
e=0
h=len(d)-1
for i in d:
    if i.isnumeric():
        e+=int(i)*(16**h)
    else:
        e+=c[i]*(16**h)
    h-=1
print('Chuỗi sau khi loại bỏ hết kí tự không thuộc b là:',b)
print('Chuỗi sau khi chuyển từ b sang số thập phân là: ',e)
