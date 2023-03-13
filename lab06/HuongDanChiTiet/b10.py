numbers = []

while True:
    number = int(input("Nhập vào một số nguyên (nhập 0 để kết thúc nhập): "))
    if number == 0:
        break
    numbers.append(number)

print("Danh sách số nguyên ban đầu:", numbers)

# a. Tìm kiếm
search_number = int(input("Nhập vào số cần tìm: "))
if search_number in numbers:
    print("Tìm thấy số", search_number, "tại vị trí",
          numbers.index(search_number) + 1)
else:
    print("Không tìm thấy số", search_number, "trong danh sách.")

# b. Chỉnh sửa
new_value = int(input("Nhập vào giá trị mới: "))
if search_number in numbers:
    index = numbers.index(search_number)
    numbers[index] = new_value
    print("Danh sách sau khi chỉnh sửa:", numbers)

# c.Thêm phần tử
new_number = int(input("Nhập vào số nguyên mới: "))
position = int(
    input("Nhập vào vị trí muốn thêm (1 - đầu, 2 - giữa, 3 - cuối): "))
if position == 1:
    numbers.insert(0, new_number)
elif position == 2:
    numbers.insert(len(numbers)//2, new_number)
else:
    numbers.append(new_number)
print("Danh sách sau khi thêm:", numbers)

# d. Sắp xếp
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Danh sách sau khi sắp xếp:", numbers)

# e.Xóa phần tử
y = int(input("Nhập phần tử cần xóa?"))
for i in range(len(numbers)):
    if numbers[i] == y:
        # Di chuyển các phần tử sau phần tử cần xóa y về trước
        for j in range(i, len(numbers)-1):
            numbers[j] = numbers[j+1]
        #n -= 1
        break

print("Trước khi xóa", numbers)
# Giảm list về kích thước mới
numbers = numbers[:len(numbers)-1]

# In list sau khi xóa
print('Sau khi xóa: ', numbers)
