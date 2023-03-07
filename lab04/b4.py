tu=int(input('Nhập tử số:'))
mau=int(input('Nhập mẫu số:'))
while mau==0:
    mau=int(input('Nhập lại mẫu số sao cho khác 0: '))
print('Phân số: {} / {}'.format(tu,mau))