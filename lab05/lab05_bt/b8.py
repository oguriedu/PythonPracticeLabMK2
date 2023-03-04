str = input("Nhập chuỗi ký tự: ")
max_char = ""
max_count = 0
for char in (str):
    count = str.count(char)
    if count > max_count:
        max_char = char
        max_count = count
print(max_char + max_count)