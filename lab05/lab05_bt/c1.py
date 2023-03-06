a=input("nhập chuỗi ký tự từ bàn phím: ")
t=0
for i in a:
    if i.isnumeric():
        print(i)
        t+=1
print(f"vậy có {t} ký tự là số trong chuỗi ký tự")
