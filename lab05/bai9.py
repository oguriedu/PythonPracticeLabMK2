str1 = input("Nhập chuỗi ký tự Str1: ")
str2 = input("Nhập chuỗi ký tự Str2: ")
chuoi_max = ""
for i in range(len(str1)):
    for j in range(len(str1)-i+1):
        # Tìm chuỗi con của str1
        chuoi_chung = str1[i:i+j]
        if chuoi_chung in str2 and len(chuoi_chung) > len(chuoi_max):
            chuoi_max = chuoi_chung

print("Chuỗi con chung của Str1 và Str2 là:", chuoi_max)
