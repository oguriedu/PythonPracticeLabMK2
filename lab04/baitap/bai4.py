# bài 4
a=int(input("nhập tử số : "))
b=int(input("nhập mẫu số : "))
while b==0:
    b=int(input('nhập lại mẫu số sao cho khác 0: '))
print('phân số:{}/{}'.format(a,b))