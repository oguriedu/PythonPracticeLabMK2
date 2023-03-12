a = []
while True:
    n = input('Nhập từng phần tử n : ')
    a.append(int(n))
    tt = input('Bạn có muốn tiếp tục? 0:không ')
    if tt == '0':
        break

print(a)
for i in a:
    assert i%2==0