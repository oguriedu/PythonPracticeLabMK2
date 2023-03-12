a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
print('tổng tất cả phần tử trong danh sách =', sum(a))
b = []
for i in a:
    if i > 0:
        b.append(i)
print('số lượng số hạng dương =', len(b))
print('tổng số hạng dương =', sum(b))
c = a.index(-4)
print('vị trí phần tử âm đầu tiên trong danh sách =', c)
d = a.index(8)
print('vị trí phần tử dương cuối cùng trong danh sách =', d)
print('phần tử lớn nhất trong danh sách =', max(a))
print('phần tử dương lớn nhất cuối cùng =', b[len(b)-1])