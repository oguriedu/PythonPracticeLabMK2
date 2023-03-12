n = int(input("Nhập số phần tử của danh sách: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

# Tìm phần tử lớn thứ nhì và các vị trí của các phần tử đạt giá trị lớn nhì.
max1 = max(lst)
max2 = float('-inf')
indices = []
for i, num in enumerate(lst):
    if num > max2 and num < max1:
        max2 = num
        indices = [i]
    elif num == max2:
        indices.append(i)
print(f"Phần tử lớn thứ nhì là {max2}, có ở các vị trí {indices}")

# Tính số lượng các số dương liên tiếp nhiều nhất.
count = 0
max_count = 0
for num in lst:
    if num > 0:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(f"Số lượng các số dương liên tiếp nhiều nhất là {max_count}")

# Tính số lượng các số dương liên tiếp có tổng lớn nhất.
count = 0
max_sum = 0
for i in range(n):
    if lst[i] > 0:
        count += lst[i]
        max_sum = max(max_sum, count)
    else:
        count = 0
print(f"Số lượng các số dương liên tiếp có tổng lớn nhất là {max_sum}")
