a=input("nhập chuỗi ký tự: ")
l=""
for i in a:
    if "0"<=i<="9" or "A"<=i<="F":
        l+=i
print(l)