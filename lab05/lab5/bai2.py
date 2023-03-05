a=input("nhập chuỗi ký tự từ bàn phím: ")
t=0
for i in a:
    if i.isnumeric() or i.isalpha():
        print(i)
        t+=1
print(len(a)-t)