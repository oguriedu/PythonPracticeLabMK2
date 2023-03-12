a = []
while True:
    n = input('Nhập phần tử: ')
    if n == '0':
        break
    a.append(n)
print(a)
b = []
for i in a:
    if i> '0':
        b.append(i)
print('danh sách phần tử dương: ',b)
m = input('thêm phần tử muốn chèn: ')
a.insert(0,m)           #chèn phần tử vào đầu list
a.insert(5,m)            #chèn phần tử vào vị trí thứ 5
a.append(m)
print(a)