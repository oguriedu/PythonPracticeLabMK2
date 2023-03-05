def count_word_occurrences(text, word):
    # Tách các từ trong đoạn văn bản thành một danh sách các từ
    words_list = text.split()
    
    # Đếm số lần xuất hiện của từ đơn trong danh sách các từ
    count = 0
    for w in words_list:
        if w == word:
            count += 1
    
    return count

# Nhập đoạn văn bản và từ đơn từ bàn phím
text = input("Nhập đoạn văn bản: ")
word = input("Nhập từ đơn: ")

# Loại bỏ các ký tự không phải chữ cái, số và dấu cách
text = ''.join(c for c in text if c.isalnum() or c.isspace())

# Chuyển tất cả các chữ hoa trong đoạn văn bản thành chữ thường để so sánh với từ đơn
text = text.lower()

# Tìm số lần xuất hiện của từ đơn trong đoạn văn bản
count = count_word_occurrences(text, word)

# In ra kết quả
print("Từ đơn '{}' xuất hiện {} lần trong đoạn văn bản.".format(word, count))

