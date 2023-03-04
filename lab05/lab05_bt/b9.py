str1 = input("Nhập chuỗi ký tự 1: ")
str2 = input("Nhập chuỗi ký tự 2: ")
result=''
for i in range(len(str1)):
    for j in range(len(str1),i-1,-1):
        if str1[i:j] in str2:
            if len(str1[i:j]) > len(result):
                result = str1[i:j]
print("Chuỗi ký tự con chung của", str1, "và", str2, "là:", result)
