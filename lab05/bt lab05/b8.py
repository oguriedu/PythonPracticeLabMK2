a=input("nhập chuỗi ký tự : ")
preindex=""
l=[]
S=""
for i in a:
    m=0
    if i != preindex :
        l.append(S)
        S=""
    S+=i
    preindex=i
else:
    l.append(S)
long1=0
long2=0
for i in l:
    long1=len(i)
    if long1>long2:
        long2=long1
for i in l:
    if len(i)==long2:
        print(i)