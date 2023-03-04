#khai báo chuỗi Str1.
Str1 = "Khoa, khoa hoc ung dung"

#sử dụng phương thức split để tách chuỗi thành list các từ dựa trên khoảng trắng
words = Str1.split(" ")

#Vòng lặp for sẽ duyệt qua từng từ có trong list words
for word in words:

#sử dụng phương thức replace để xóa dấu phẩy (nếu có) trong từ đang xét
    word = word.replace(",", "")

print(word)
