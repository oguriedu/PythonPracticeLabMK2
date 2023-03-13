a = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để dừng nhập): "))
    if num == 0:
        break
    a.append(num)
print(a)

# Chuyển các phần tử dương lên đầu danh sách
a.sort(reverse=True)
print(a)

# Chèn số m vào đầu danh sách
m = int(input("Nhập m: "))
a.insert(0, m)
print(a)

# Chèn số m vào cuối danh sách
a.append(m)
print(a)

# Chèn số m vào vị trí thứ 5 của danh sách
a.insert(4, m)
print(a)
