str=input('Nhập 1 chuỗi ký tự: ')
a=''
for c in str:
    if '0'<= c <='9'or 'A'<=c<='F':
        a+=c
if len(str)==len(a):
    print('Chuỗi trên là chuỗi được viết trong hệ Hex ')
else:
    print('Chuỗi sau khi loại bỏ các kí tự không có trong hệ Hex :',a)
m=['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
d=0
for i in range(0,len(a)):
    b=n[m.index(a[i])]*(16**(len(a)-1-i))
    d+=b
print('Chuyển sang hệ thập phân:',d)
