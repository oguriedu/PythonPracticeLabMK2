# Nhập chuỗi ký tự Str từ bàn phím
Str = input("Nhập chuỗi ký tự: ")

# Khởi tạo biến lưu chuỗi con dài nhất và biến đếm độ dài của chuỗi con hiện tại
longest_str = ""
current_str = Str[0]

# Duyệt qua chuỗi Str
for i in range(1, len(Str)):
    if Str[i] == Str[i-1]:
    
        current_str += Str[i]
    else:
        # Nếu không, so sánh độ dài của chuỗi con hiện tại với chuỗi con dài nhất
        if len(current_str) > len(longest_str):
            longest_str = current_str
        # Khởi tạo chuỗi con mới bằng ký tự hiện tại
        current_str = Str[i]

# Kiểm tra nếu chuỗi con hiện tại có độ dài lớn hơn chuỗi con dài nhất đã tìm được
if len(current_str) > len(longest_str):
    longest_str = current_str

print("Chuỗi ký tự con dài nhất chứa các ký tự giống nhau của chuỗi '", Str, "' là:", longest_str)
