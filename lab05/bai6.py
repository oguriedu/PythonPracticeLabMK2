str=input("nhập chuỗi ký tự: ")
b=""
for i in str:
    if "0"<=i<="9" or "A"<=i<="F":
        b+=i
print(b)