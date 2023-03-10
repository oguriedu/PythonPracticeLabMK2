Str = input("Nhập chuỗi văn bản: ")
word = input("Nhập từ đơn cần tìm: ")
words = Str.split() 
count = 0
for w in words:
    if w == word:
        count += 1
print(f"Từ '{word}' xuất hiện {count} lần trong chuỗi văn bản.")