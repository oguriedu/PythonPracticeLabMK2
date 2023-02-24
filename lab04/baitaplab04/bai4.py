from fractions import*
a = int(input('Nhập tử số: '))
b = int(input('Nhập mẫu số: '))
while b==0:
    b = int(input('Nhập lại mẫu số: '))
    break
phan_so = Fraction(a,b)
print('phân số vừa nhập là: ',phan_so)