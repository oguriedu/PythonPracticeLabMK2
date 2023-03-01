words = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
num = int(input("Nhập số cần chuyển đổi: "))
for digit in str(num):
    print(words[int(digit)], end=' ')
