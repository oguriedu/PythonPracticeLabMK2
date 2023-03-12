# Nhập danh sách các số nguyên từ bàn phím
lst = []
while True:
    n = int(input("Nhập số nguyên (nhập 0 để kết thúc): "))
    if n == 0:
        break
    lst.append(n)

# Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách
lst = [1,2,3] + lst + [1,2,3] + lst[4:]

print("Danh sách mới sau khi chèn danh sách [1,2,3]:", lst)

# Xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách
k = int(input("Nhập vị trí phần tử cần xóa: "))
del lst[k-1]

print("Danh sách mới sau khi xóa phần tử thứ", k, ":", lst)

# Sắp xếp danh sách theo thứ tự tăng dần, giảm dần
lst.sort()
print("Danh sách mới sau khi sắp xếp tăng dần:", lst)

lst.sort(reverse=True)
print("Danh sách mới sau khi sắp xếp giảm dần:", lst)