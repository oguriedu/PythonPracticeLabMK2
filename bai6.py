# Khởi tạo mảng chứa các từ tương ứng với các chữ số từ 0 đến 9
words = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

# Nhập số từ bàn phím
num = int(input("Nhập số cần chuyển đổi: "))

# Chuyển đổi số thành chuỗi và in từng chữ số tương ứng
for digit in str(num):
    print(words[int(digit)], end=' ')
