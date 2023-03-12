n=input('Nhập các chuỗi mật khẩu tách nhau bởi dấu phảy: ')
a=n.split(',')
b=[]
for i in a:
    thuong=0
    hoa=0
    so=0
    db=0
    for j in i:
        if 'a'<=j<='z':
            thuong+=1
        elif 'A'<=j<='Z':
            hoa+=1
        elif '0'<=j<='9':
            so+=1
        elif j=='$'or j=='@'or j=='#':
            db+=1
    if 6<=len(i)<=12 and thuong>=1 and hoa>=1 and so>=1 and db>=1:
        b.append(i)
print(f'Mật khẩu hợp lệ: {b}')