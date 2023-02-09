a=input("nhập tọa độ A(phân cách bởi giấu ','): ")
b=input("nhập tọa độ B(phân cách bởi giấu ','): ")
m=a.split(",")
n=b.split(",")
t=0
for i in range (0,len(m)):
    t+=int(m[i])*int(n[i])
print("Tích vô hướng của A và B: ",t)