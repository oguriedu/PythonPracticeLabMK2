a=input("nhập chuỗi ký tự: ")
preindex=""
l=[]
k=""
for i in a:
    m=0
    if i != preindex :
        l.append(k)
        k=""
    k+=i
    preindex=i
else:
    l.append(k)
long1=0
long2=0
for i in l:
    long1=len(i)
    if long1>long2:
        long2=long1
for i in l:
    if len(i)==long2:
        print(i)
