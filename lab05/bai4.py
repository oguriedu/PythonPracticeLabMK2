str1 = input("Nhập chuỗi ký tự 1: ")
str2 = input("Nhập chuỗi ký tự 2: ")

merged_str = ''
for i in range(max(len(str1), len(str2))):
    if i < len(str1):
        merged_str += str1[i]
    if i < len(str2):
        merged_str += str2[i]

print("Chuỗi ký tự sau khi trộn là:", merged_str)
