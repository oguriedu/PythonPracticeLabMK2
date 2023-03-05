n=input('Nhập văn bản:')
m=0
for i in n:
    c=n.count(i)
    max=m
    if c > m:
        m=c
for j in n:
    if n.count(j)==m:
        print(end=j)