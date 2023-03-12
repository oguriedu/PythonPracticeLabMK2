a = []
while True:
    n = int(input('Nhập phần tử: '))
    if n == 0:
        break
    a.append(n)
b = [1,2,3]
copy = a.copy()
copy.insert(0,b)
copy.insert(5,b)
copy.append(b)
print(copy)
k = int(input('Nhập phần tử muốn xóa: '))
del(copy[k])
print('list sau khi xóa phần tử thứ k là: ',copy)
lst = a + b
print(lst)
lst.sort()
print('list sắp xếp tăng dần là: ',lst )
lst.sort()
lst.reverse()
print('list sắp xếp giảm dần là: ',lst)
