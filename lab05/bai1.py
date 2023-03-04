Str = input("Nhập chuỗi ký tự: ")

count = 0
for char in Str:
    if char.isdigit():
        count += 1

print("Số lượng ký tự số trong chuỗi là:", count)
