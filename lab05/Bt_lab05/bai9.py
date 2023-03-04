#Chua ht nốt
str1 = input("Nhập chuỗi ký tự Str1: ")
str2 = input("Nhập chuỗi ký tự Str2: ")
bd_str = ""
for i in range(min(len(str1), len(str2))):
    if str1[i] == str2[i]:
        bd_str += str1[i]
    else:
        break
print("Chuỗi con chung của Str1 và Str2 là:", bd_str)
