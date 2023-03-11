# Khởi tạo danh sách rỗng
lst = []

# Nhập các phần tử cho đến khi gặp phần tử 0
while True:
    x = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if x == 0:
        break
    lst.append(x)

# Chèn danh sách [1, 2, 3] vào vị trí đầu, cuối và thứ 5
lst = [1, 2, 3] + lst           # chèn vào đầu
lst = lst + [1, 2, 3]           # chèn vào cuối
lst.insert(4, [1, 2, 3])        # chèn vào vị trí thứ 5

# In danh sách sau khi chèn
print("Danh sách sau khi chèn: ", lst)

# Xóa phần tử thứ k (k nhập từ bàn phím)
k = int(input("Nhập vị trí phần tử cần xóa: "))
del lst[k-1]

# In danh sách sau khi xóa
print("Danh sách sau khi xóa: ", lst)

# Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
lst.sort()
print("Danh sách theo thứ tự tăng dần: ", lst)

lst.sort(reverse=True)
print("Danh sách theo thứ tự giảm dần: ", lst)
