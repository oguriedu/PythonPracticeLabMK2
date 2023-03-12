list = []
while True:
    n = int(input('Nhập phần tử vào list: '))
    list.append(n)
    if n == 0:
        print('Kết thúc nhập')
        break
print('List cần thao tác là:',list)

listcl = list.copy()
listcl.sort(reverse=True)
print('List sau khi sắp xếp là:',listcl)

m = int(input('Nhập số cần chèn vào list: '))
list.append(m)
list.insert(0, m)
list.insert(5, m)
print(list)
