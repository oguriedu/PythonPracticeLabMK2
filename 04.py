#Nhập phân số
a=int(input("nhập tử số : "))
b=int(input("nhập mẫu số : "))
while b==0:
    b=int(input('Nhập lại mẫu số sao cho khác 0: '))
print('Phân số: {} / {}'.format(a,b))
