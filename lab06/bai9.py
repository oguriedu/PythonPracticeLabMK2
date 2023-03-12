ls = []
while True:
    a = int(input('nhập phần tử trong list(nhập 0 để dừng lại):'))
    if a == 0:
        break
    else:
        ls.append(a)
print('list vừa nhập',ls)
#dùng assert
for i in ls:
    assert i % 2 == 0, ' có chứa số lẻ'
print('tất cả các số trong dãy là chẵn')
