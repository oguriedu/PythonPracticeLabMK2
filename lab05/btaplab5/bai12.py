a=input("nhập chuỗi A: ")
b=input("nhập chuỗi B: ")
sta=0
stb=0
l=[]
for i in a:
    sta+=1
    stb=1
    if sta>=len(a) or stb>=len(b):
            break
    xa=int(a[0:sta])
    ma=int(a[int(sta):int(len(a))])
    for ib in b:
        if sta>=len(a) or stb>=len(b):
            break
        xb=int(b[0:stb])
        mb=int(b[int(stb):int(len(b))])
        if xa+ma==xb+mb:
            h=f'{xa}+{ma}=={xb}+{mb}'
            l.append(h)
        stb+=1
if len(l)==0:
     print("không tồn tại cách đặt")
else:
     for i in l:
        print(i)
