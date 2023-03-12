ls = []
while True:
    a = int(input('nhập phần tử trong list(nhập 0 để dừng lại):'))
    if a == 0:
        break
    else:
        ls.append(a)
print('list vừa nhập',ls)

ls.sort()
print('list sau chuyển đổi',ls)
m = int(input('nhập giá trị m chèn vào list:'))
ls.insert(0,m)
ls.insert(4,m)
ls.append(m)

print(ls)

    
