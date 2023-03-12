n = int(input("Nhập số phần tử của danh sách: "))
lst = []
for i in range(n):
    lst.append(int(input("Nhập phần tử thứ {}:".format(i+1))))

#Tìm phần tử lớn thứ nhì 
max_num = max(lst)
second_max = -float("inf")
for num in lst:
    if num > second_max and num < max_num:
        second_max = num

print("Phần tử lớn thứ nhì của danh sách là:", second_max)

#Tìm vị trí các phần tử đạt giá trị lớn nhì
positions = []
for i, num in enumerate(lst):
    if num == second_max:
        positions.append(i)

print("Các vị trí của các phần tử đạt giá trị lớn nhì là:", positions)

#Tìm số lượng các số dương liên tiếp nhiều nhất
max_consecutive_count = 0
consecutive_count = 0
for num in lst:
    if num > 0:
        consecutive_count += 1
    else:
        if consecutive_count > max_consecutive_count:
            max_consecutive_count = consecutive_count
        consecutive_count = 0

if consecutive_count > max_consecutive_count:
    max_consecutive_count = consecutive_count

print("Số lượng các số dương liên tiếp nhiều nhất là:", max_consecutive_count)

#Tìm số lượng các số dương liên tiếp có tổng lớn nhất
max_sum_count = 0
start = 0
end = 0
for i in range(n):
    if lst[i] > 0:
        j = i
        current_sum = 0
        while j < n and lst[j] > 0:
            current_sum += lst[j]
            j += 1
        if current_sum > max_sum_count:
            max_sum_count = current_sum
            start = i
            end = j - 1

print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", end - start + 1)
