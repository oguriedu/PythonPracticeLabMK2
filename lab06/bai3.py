# Khởi tạo danh sách rỗng
lst = []

# Nhập vào danh sách các số tự nhiên, kết thúc khi nhập vào số 0
while True:
    n = int(input("Nhập số tự nhiên (0 để kết thúc): "))
    if n == 0:
        break
    lst.append(n)

# In danh sách ban đầu
print("Danh sách ban đầu:", lst)

# Chuyển các phần tử dương lên đầu danh sách
lst = [x for x in lst if x > 0] + [x for x in lst if x <= 0]

# In danh sách sau khi chuyển các phần tử dương lên đầu danh sách
print("Danh sách sau khi chuyển các phần tử dương lên đầu danh sách:", lst)

# Nhập vào số m từ bàn phím
m = int(input("Nhập số m: "))

# Chèn số m vào đầu danh sách
lst.insert(0, m)

# Chèn số m vào cuối danh sách
lst.append(m)

# Chèn số m vào vị trí thứ 5 của danh sách
lst.insert(4, m)

# In danh sách sau khi chèn số m vào đầu, cuối và vị trí thứ 5 của danh sách
print("Danh sách sau khi chèn số m vào đầu, cuối và vị trí thứ 5 của danh sách:", lst)
