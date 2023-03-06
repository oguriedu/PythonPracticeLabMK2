str = input("Nhập một chuỗi kí tự: ")
count = 0
for char in str:
    if not char.isalpha() and not char.isdigit():
        count += 1
