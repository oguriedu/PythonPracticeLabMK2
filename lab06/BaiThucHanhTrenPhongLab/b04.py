a = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để dừng nhập): "))
    if num == 0:
        break
    a.append(num)
print(a)

# Chèn danh sách [1, 2, 3] vào vị trí đầu, cuối và thứ 5 của danh sách
b = [1, 2, 3]
a = b + a
a = a + b
for i in range(len(b) - 1, -1, -1):
    a.insert(4, b[i])
print(a)

# Xóa phần tử thứ k (k nhập từ bàn phím)
k = int(input("Nhập vị trí k: "))
del a[k-1]
print(a)

# Sắp xếp danh sách theo thứ tự tăng dần, giảm dần
a.sort()
print("Danh sách tăng dần:", a)
a.sort(reverse=True)
print("Danh sách giảm dần:", a)
