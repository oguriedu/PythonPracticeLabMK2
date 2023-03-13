# c1
# Nhập chuỗi s từ bàn phím
s = input("Nhập chuỗi: ")

# Khởi tạo biến đếm số chữ cái
count = 0

# Duyệt từng ký tự trong chuỗi s
for char in s:
    # Kiểm tra xem ký tự đó có phải là chữ cái không
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        count += 1

# Xuất ra kết quả
print("Số chữ cái trong chuỗi là:", count)

# c2
# Nhập chuỗi
S = input("Nhập chuỗi: ")

# Khởi tạo biến đếm
count = 0
# Duyệt từng ký tự của chuỗi
for char in S:
    # Nếu ký tự là chữ cái tiếng Anh (bao gồm cả hoa, thường)
    if char.isalpha():
        count += 1
# In kết quả
print("Số chữ cái tiếng Anh trong chuỗi:", count)
