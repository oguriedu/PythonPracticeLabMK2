ls = []
while True:
    a = int(input('nhập phần tử trong list(nhập 0 để dừng lại):'))
    if a == 0:
        break
    else:
        ls.append(a)
print('list vừa nhập',ls)
a = [1,2,3]
ls.insert(0,a)
ls.insert(5,a)
ls.append(a)
print('list sau chỉnh sửa',ls)

k = int(input('nhập thứ tự k muốn xóa:'))
ls.pop(k)
print('list mới = ',ls)
ls.sort()
print('list sắp xếp tăng dần',ls)
ls.reverse()
print('list xắp sếp giảm dần = ',ls)

