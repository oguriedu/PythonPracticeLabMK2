str=input("nhập chuỗi: ")
a=0
for i in str:
    dem=str.count(i)
    max=a
    if dem>a:
        a=dem
for j in str:
    if str.count(j)==a:
        print(end=j)