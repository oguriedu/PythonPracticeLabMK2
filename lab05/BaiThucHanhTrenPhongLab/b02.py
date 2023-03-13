str = input("Nhập chuỗi ký tự: ")
count = 0

for char in str:
    if char.isdigit() == False and char.isalpha() == False:
        count += 1

print("Số ký tự không phải chữ cái tiếng Anh và không là số trong chuỗi là: ", count)
