str_1 = input("Nhập chuỗi 1: ")
str_2 = input("Nhập chuỗi 2: ")

common_substrings = []

for i in range(len(str_1)):
    for j in range(i+1, len(str_1)+1):
        if str_1[i:j] in str_2:
            common_substrings.append(str_1[i:j])

max_len = 0
for i in common_substrings:
    if len(i) > max_len:
        max_len = len(i)

for i in common_substrings:
    if len(i) == max_len:
        print(i)