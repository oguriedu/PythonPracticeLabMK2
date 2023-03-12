a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# tính tổng các phần tử của danh sách
sum_a = sum(a)
print("Tổng các phần tử của danh sách là:", sum_a)

# đếm số lượng các số hạng dương và tổng của các số hạng dương
count_positive = sum_positive = 0
for i in a:
    if i > 0:
        count_positive += 1
        sum_positive += i
print("Số lượng các số hạng dương là:", count_positive)
print("Tổng các số hạng dương là:", sum_positive)

# tìm vị trí của phần tử âm đầu tiên trong danh sách
index_negative = None
for i in range(len(a)):
    if a[i] < 0:
        index_negative = i
        break
if index_negative is not None:
    print("Vị trí của phần tử âm đầu tiên là:", index_negative)
else:
    print("Không có phần tử âm trong danh sách")

# tìm vị trí của phần tử dương cuối cùng trong danh sách
index_last_positive = None
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        index_last_positive = i
        break
if index_last_positive is not None:
    print("Vị trí của phần tử dương cuối cùng là:", index_last_positive)
else:
    print("Không có phần tử dương trong danh sách")

# tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
max_value = max(a)
index_last_max = len(a) - a[::-1].index(max_value) - 1
print("Phần tử lớn nhất của danh sách là:", max_value)
print("Vị trí phần tử lớn nhất cuối cùng là:", index_last_max)
