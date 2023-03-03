word = input("Nh ập vào một từ đơn: ") 
Str = "Các từ 'nhà', 'xe', 'cây','mắt','bàn','ghế','núi','rừng',... chính là từ đơn."

count = 0 
for w in Str.split(): 
    if w == word: count += 1

print("Chuỗi Str có chứa", count, "từ đơn", word)