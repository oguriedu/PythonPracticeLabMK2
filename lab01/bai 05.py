a = input("nhập tọa độ A(phân cách bởi giấu ','): ")
b = input("nhập tọa độ B(phân cách bởi giấu ','): ")
c = a.split(",")
d = b.split(",")
e = 0
for i in range (0,len(c)):
    e+=int(c[i])*int(d[i])
print("Tích vô hướng của A và B: ",e)
