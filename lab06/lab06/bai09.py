a=(2,2,2,4,2,6)
chan=0
for i in a:
    if i%2==0:
        chan+=1
assert chan!=len(a),"chuỗi toàn chẵn"