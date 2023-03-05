Str = input("Nhập chuỗi ký tự Str: ")
n = len(Str)

max_len = 0
result = ""

for i in range(n):
    count = 1
    for j in range(i+1, n):
        if Str[j] == Str[i]:
            count += 1
        else:
            break
    if count > max_len:
        max_len = count
        result = Str[i:i+count]

print("Chuỗi con có độ dài cực đại và bao gồm các phần tử giống nhau của chuỗi Str là:", result)
