Str1 = input("Nhập chuỗi ký tự 1: ")
Str2 = input("Nhập chuỗi ký tự 2: ")

merged_str = ''
for i in range(max(len(Str1), len(Str2))):
    if i < len(Str1):
        merged_str += Str1[i]
    if i < len(Str2):
        merged_str += Str2[i]

print("Chuỗi ký tự sau khi trộn là:", merged_str)
