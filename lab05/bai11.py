#in danh sách từ, mỗi từ một dòng
Str1 = input("nhập chuỗi kí tự bạn muốn xử lí = ")
tu = Str1.split(' ') 
for word in tu:
    word = word.replace(',', '')
    print(word)
