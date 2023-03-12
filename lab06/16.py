X = int(input("Nhập giá trị X: ")) # Nhập giá trị X
Y = int(input("Nhập giá trị Y: ")) # Nhập giá trị Y

array_2d = [] # Khởi tạo mảng 2 chiều rỗng

# Tạo mảng 2 chiều với giá trị phần tử là i*j
for i in range(X):
    row = []
    for j in range(Y):
        row.append(i*j)
    array_2d.append(row)

# In mảng 2 chiều
print(array_2d)
