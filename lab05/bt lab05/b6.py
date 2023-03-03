a=input("nhập chuỗi ký tự : ")
s=""
for i in a:
    if "0"<=i<="9" or "A"<=i<="F":
        s+=i
print(s)