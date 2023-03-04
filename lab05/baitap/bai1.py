#bai 1:
str=input("nhập chuỗi ký tự từ bàn phím: ")
a=0
for i in str:
    if i.isalnum():
        print(i)
        a+=1
print(f"vậy có {a} ký tự là số trong chuỗi ký tự.")