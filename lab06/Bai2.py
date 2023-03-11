n = int(input("Nhập số phần tử của danh sách: "))
numbers = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    numbers.append(num)

print("Danh sách vừa nhập là:", numbers)
# tìm phần tử lớn thứ nhì của danh sách và các vị trí của các phần tử đạt giá trị lớn nhì.
unique_lst = list(set(numbers))
if len(unique_lst) == 1:
    print("Phần tử lớn thứ nhì không tồn tại!")
else:
    unique_lst.sort(reverse=True)
    second_largest = unique_lst[1]
    print("Phần tử lớn thứ nhì là:", second_largest)
    b = [i for i in range(len(numbers)) if numbers[i] == second_largest]
    print("Các vị trí của các phần tử đạt giá trị lớn nhì là:", b)
#Tính số lượng các số dương liên tiếp nhiều nhất
count = 0
max_count = 0
for num in numbers:
    if num > 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0 
print("Số lượng các số dương liên tiếp nhiều nhất là:", max_count)

 #Tính số lượng các số dương liên tiếp có tổng lớn nhất.
count = 0
max_count = 0
max_sum = 0
for num in numbers:
    if num > 0:
        count += 1
        if count > max_count:
            max_count = count
            max_sum = num * count
        elif count == max_count: 
            if num * count > max_sum:
                max_sum = num * count
    else:
        count = 0
print("Số lượng các số dương liên tiếp có tổng lớn nhất là:", max_count)


