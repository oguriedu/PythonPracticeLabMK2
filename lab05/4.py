Str1 = input("Nhập chuỗi Str1: ")
Str2 = input("Nhập chuỗi Str2: ")

result = ""
i = 0
j = 0

while i < len(Str1) and j < len(Str2):
    result += Str1[i]
    result += Str2[j]
    i += 1
    j += 1

while i < len(Str1):
    result += Str1[i]
    i += 1

while j < len(Str2):
    result += Str2[j]
    j += 1

print("Kết quả trộn chuỗi Str1 và Str2: ", result)
