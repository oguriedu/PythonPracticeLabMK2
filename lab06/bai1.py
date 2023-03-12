# Khai báo danh sách
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# Tính tổng các phần tử của danh sách
sum_a = sum(a)
print("Tổng các phần tử của danh sách là:", sum_a)

# Đếm số lượng số hạng dương và tính tổng các số hạng dương
count_positive = 0
sum_positive = 0
for num in a:
    if num > 0:
        count_positive += 1
        sum_positive += num
print("Số lượng số hạng dương là:", count_positive)
print("Tổng các số hạng dương là:", sum_positive)

# Tìm vị trí của phần tử âm đầu tiên trong danh sách
index_first_negative = -1
for i, num in enumerate(a):
    if num < 0:
        index_first_negative = i
        break
if index_first_negative == -1:
    print("Không có phần tử âm trong danh sách")
else:
    print("Vị trí của phần tử âm đầu tiên là:", index_first_negative)

# Tìm vị trí của phần tử dương cuối cùng trong danh sách
index_last_positive = -1
for i, num in enumerate(a):
    if num > 0:
        index_last_positive = i
if index_last_positive == -1:
    print("Không có phần tử dương trong danh sách")
else:
    print("Vị trí của phần tử dương cuối cùng là:", index_last_positive)

# Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
max_num = max(a)
index_last_max = -1
for i, num in enumerate(a):
    if num == max_num:
        index_last_max = i
print("Phần tử lớn nhất của danh sách là:", max_num)
print("Vị trí phần tử lớn nhất cuối cùng là:", index_last_max)
