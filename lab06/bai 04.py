lst = []
while True:
    x = int(input('Nhập một số tự nhiên (nhập 0 để kết thúc): '))
    if x == 0:
        break
    lst.append(x)
lst = [1, 2, 3] + lst
lst = lst + [1, 2, 3]
lst.insert(4, [1, 2, 3])
print('Danh sách sau khi chèn:', lst)
k = int(input('Nhập vị trí phần tử cần xóa: '))
del lst[k-1]
print('Danh sách sau khi xóa:', lst)
lst.sort()
print('Danh sách theo thứ tự tăng dần:', lst)
lst.sort(reverse=True)
print('Danh sách theo thứ tự giảm dần:', lst)
