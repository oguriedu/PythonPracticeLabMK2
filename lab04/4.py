tu_so=int(input('Nhập tử số:'))
mau_so=int(input('Nhập mẫu số:'))
while mau_so==0:
    mau_so=int(input('Nhập lại mẫu số sao cho khác 0: '))
print('Phân số: {} / {}'.format(tu_so,mau_so))