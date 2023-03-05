Str = input("Nhập chuỗi ký tự: ")
count = 0
for char in Str:
   
    if not char.isalpha() and not char.isdigit():
        count += 1

print("Số lượng ký tự không phải là chữ cái tiếng Anh và không là số trong chuỗi Str: " + str(count))
