str1 = input("Nhập chuỗi ký tự 1: ")
str2 = input("Nhập chuỗi ký tự 2: ")

len_str1 = len(str1)
len_str2 = len(str2)
min_len = min(len_str1, len_str2)
result = ""
for i in range(min_len):
    result = result + str1[i] + str2[i]
if len_str1 > len_str2:
    result = result + str1[min_len:]
else:
    result = result + str2[min_len:]
print(result)
