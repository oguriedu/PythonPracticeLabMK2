# Nhập đoạn văn bản từ bàn phím
str = input("Nhập đoạn văn bản: ")
tu_don = input("Nhập từ cần tìm: ")
text = str.split()
# Đếm số lần xuất hiện của từ đơn trong đoạn văn bản
count = 0
for c in text:
    if c == text:
        count += 1

print("Từ", tu_don, "xuất hiện", count, "lần trong đoạn văn bản.")
