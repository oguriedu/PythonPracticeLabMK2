str1 = input("Nhập chuỗi ký tự Str1: ")
str2 = input("Nhập chuỗi ký tự Str2: ")

# Khởi tạo chuỗi con chung của 2 chuỗi
common_str = ""

# Tìm ra chuỗi con chung của 2 chuỗi
for i in range(min(len(str1), len(str2))):
    if str1[i] == str2[i]:
        common_str += str1[i]
    else:
        break
 
# In ra chuỗi con chung của 2 chuỗi
print("Chuỗi con chung của Str1 và Str2 là:", common_str)