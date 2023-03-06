str = input("Nhập chuỗi ký tự Str: ")
n = len(str)

max_len = 0
result = ""

for i in range(n):
    count = 1
    for j in range(i+1, n):
        if str[j] == str[i]:
            count += 1
        else:
            break
    if count > max_len:
        max_len = count
        result = str[i:i+count]

print("Chuỗi con có độ dài cực đại và bao gồm các phần tử giống nhau của chuỗi Str là:", result)
