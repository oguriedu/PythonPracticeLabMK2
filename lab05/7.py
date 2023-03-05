# Nhập chuỗi văn bản Str từ bàn phím
Str = input("Nhập chuỗi văn bản: ")

# Nhập từ đơn cần tìm từ bàn phím
word = input("Nhập từ đơn cần tìm: ")

# Tách chuỗi Str thành danh sách các từ
word_list = Str.split()

# Khởi tạo biến đếm số từ đơn
count = 0

# Duyệt danh sách các từ và đếm số từ đơn cần tìm
for w in word_list:
    if w == word:
        count += 1

# In ra kết quả
print("Số lần xuất hiện của từ '", word, "' là:", count)
