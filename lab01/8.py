# tìm tào độ tâm abc
a= float(input(" nhập đỉnh thứ nhất:"))
b= float(input(" nhập đỉnh thứ hai:"))
c= float(input(" nhập đỉnh thứ ba:"))
tda=a.split(";")
tdb=b.split(";")
tdc=c.split(";")
g=[]
for i in range (len(tda)):
    m=(int(tda[i])+int(tdb[i])+int(tdc[i])/3)
    g.append(m)
print("Tọa độ trọng tâm tam giác ABC là",g)