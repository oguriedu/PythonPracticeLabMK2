# Hàm chuyển các phần tử dương của danh sách lên đầu danh sách
def move_positive_numbers_to_beginning(lst):
    i = 0
    j = len(lst) - 1
    while i <= j:
        if lst[i] < 0 and lst[j] > 0:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        elif lst[i] > 0:
            i += 1
        else:
            j -= 1

# Hàm chèn một số vào đầu danh sách
def insert_at_beginning(lst, num):
    lst.insert(0, num)

# Hàm chèn một số vào cuối danh sách
def insert_at_end(lst, num):
    lst.append(num)

# Hàm chèn một số vào vị trí thứ 5 của danh sách
def insert_at_pos_5(lst, num):
    lst.insert(4, num)

# Nhập vào danh sách từ bàn phím
lst = []
while True:
    num = int(input("Nhập số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break
    lst.append(num)

# Hiển thị danh sách ban đầu
print("Danh sách ban đầu:")
print(lst)

# Di chuyển các phần tử dương lên đầu danh sách
move_positive_numbers_to_beginning(lst)

# Hiển thị danh sách sau khi di chuyển phần tử dương lên đầu danh sách
print("Danh sách sau khi di chuyển phần tử dương lên đầu danh sách:")
print(lst)

# Chèn một số vào đầu danh sách
num = int(input("Nhập số cần chèn vào đầu danh sách: "))
insert_at_beginning(lst, num)

# Hiển thị danh sách sau khi chèn số vào đầu danh sách
print("Danh sách sau khi chèn số vào đầu danh sách:")
print(lst)

# Chèn một số vào cuối danh sách
num = int(input("Nhập số cần chèn vào cuối danh sách: "))
insert_at_end(lst, num)

# Hiển thị danh sách sau khi chèn số vào cuối danh sách
print("Danh sách sau khi chèn số vào cuối danh sách:")
print(lst)

# Chèn một số vào vị trí thứ 5 của danh sách
num = int(input("Nhập số cần chèn vào vị trí thứ 5 của danh sách: "))
insert_at_pos_5(lst, num)

# Hiển thị danh sách sau khi chèn số vào vị trí thứ 5 của danh sách
print("Danh sách sau khi chèn số vào vị trí thứ 5 của danh sách:")
print(lst)
