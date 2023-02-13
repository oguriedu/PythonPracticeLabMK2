a=input("nhập đỉnh A: ")
b=input("nhập đỉnh B: ")
c=input("nhập đỉnh C: ")
tda=a.split(";")
tdb=b.split(";")
tdc=c.split(";")
h=[]
for i in range (len(tda)):
    m=(int(tda[i])+int(tdb[i])+int(tdc[i])/3)
    h.append(m)
print("tọa độ trọng tâm tam giác ABC là",h)