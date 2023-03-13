n = input("Nhập chuỗi ký tự: ")
count = 1
max_count = 1
result = n[0]
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        count += 1
    else:
        if count >= max_count:
            max_count = count
            result = n[i-count:i]
        count = 1
if count >= max_count:
    max_count = count
    result = n[-count:]
print("Chuỗi ký tự con có độ dài cực đại và bao gồm các phần tử giống nhau của chuỗi ký tự là:", result)
