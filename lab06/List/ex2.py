n=int(input("Nhập số phần tử của danh sách:"))
lst=[]
for i in range(n):
    lst.append(int(input(f"Nhập phần tử thứ {i+1}:")))
print(lst)
max1 = max2 = lst[0]
pos = [1]
for i in range(1, n):
    if lst[i] > max1:
        max2 = max1
        max1 = lst[i]
        pos = [i+1]
    elif lst[i] == max1:
        pos.append(i+1)
    elif lst[i] > max2:
        max2 = lst[i]

print("Phần tử lớn thứ nhì là:", max2)
print("Các vị trí của phần tử lớn thứ nhì là:", pos)


count = max_count = 0
for i in range(n):
    if lst[i] > 0:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print("Số lượng các số dương liên tiếp nhiều nhất là:", max_count)

count = max_count = max_sum = 0
for i in range(n):
    if lst[i] > 0:
        count += 1
        max_sum += lst[i]
        if count > max_count:
            max_count = count
            max_sum = sum(lst[i-max_count+1:i+1])
        elif count == max_count:
            max_sum = max(max_sum, sum(lst[i-max_count+1:i+1]))
    else:
        count = 0

print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", max_count)
print("Tổng của các số dương liên tiếp có tổng lớn nhất là:", max_sum)