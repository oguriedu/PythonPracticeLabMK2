a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
# Tính tổng các phần tử của danh sách
print(f"Tổng các phần tử của danh sách là {sum(a)}")

# Đếm số lượng các số hạng dương và tổng của các số hạng dương
count = 0
sum = 0
for num in a:
    if num > 0:
        count = count + 1
        sum = sum + num
print(
    f"Số lượng các số hạng dương là {count} và tổng của các số hạng dương là {sum}")

# Tìm vị trí của phần tử âm đầu tiên trong danh sách
num_index = None
for i in range(0, len(a), 1):
    if a[i] < 0:
        num_index = i
        break
print(
    f"Vị trí của phần tử âm đầu tiên trong danh sách là {num_index}")

# Tìm vị trí của phần tử dương cuối cùng trong danh sách
num_index = None
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        num_index = i
        break
print(
    f"Vị trí của phần tử dương cuối cùng trong danh sách là {num_index}")

# Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
max_num = max(a)
max_num_index = None
for i in range(len(a)-1, -1, -1):
    if a[i] == max_num:
        max_num_index = i
        break
print(
    f"Phần tử lớn nhất của danh sách là {max_num} và vị trí phần tử lớn nhất cuối cùng là {max_num_index}")
