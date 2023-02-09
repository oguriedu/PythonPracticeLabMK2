
a=input("nhập tọa độ A(x,y phân cách bởi giấu ';'): ")
b=input("nhập tọa độ B(x,y phân cách bởi giấu ';'): ")
tda=a.split(";")
tdb=b.split(";")
t=0
for i in range (len(tda)):
    t+=int(tda[i-1])*int(tdb[i-1])
print("tích vô hướng của A và B: ",t)