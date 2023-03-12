str=input("Nhập chuỗi: ")
max=0
for i in str:
    a=str.count(i)
    if a>max:
        max=a
for i in str:
    if str.count(i)==max:
        print(i,end='')