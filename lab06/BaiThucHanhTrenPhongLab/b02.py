n = int(input("Nhập số phần tử của danh sách: "))
a = []
for i in range(n):
    while True:
        num = int(input(f"Nhập phần tử thứ {i+1}: "))
        if num >= 0:
            break
    a.append(num)

# Tìm phần tử lớn thứ nhì và các vị trí của các phần tử đạt giá trị lớn nhì
max_num = max(a)
second_max_num = -1
second_max_num_index = []
for num in a:
    if num < max_num and num > second_max_num:
        second_max_num = num
for num in a:
    if num == second_max_num:
        second_max_num_index.append(a.index(num))
print(
    f"Phần tử lớn thứ nhì của danh sách là {second_max_num} và các vị trí của các phần tử đạt giá trị lớn nhì là {second_max_num_index}")

# Tính số lượng các số dương liên tiếp nhiều nhất
max_count = 0
current_count = 0
for num in a:
    if num > 0:
        current_count = current_count + 1
        max_count = max(
            max_count, current_count)
    else:
        current_count = 0
print(
    f"Số lượng các số dương liên tiếp nhiều nhất là {max_count}")

# Tính số lượng các số dương liên tiếp có tổng lớn nhất
max_sum = 0
current_sum = 0
max_sum_count = 0
current_sum_count = 0
for num in a:
    if num > 0:
        current_sum = current_sum + num
        current_sum_count = current_sum_count + 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_count = current_sum_count
        elif current_sum == max_sum:
            max_sum_count = max(
                max_sum_count, current_sum_count)
    else:
        current_sum = 0
        current_sum_count = 0
print(
    f"Số lượng các số dương liên tiếp có tổng lớn nhất là {max_sum_count}")
