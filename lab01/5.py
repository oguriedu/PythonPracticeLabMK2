#Nhập vector a
a = list(map(int, input("Nhập vector a: ").split())) 

#Nhập vector b
b = list(map(int, input("Nhập vector b: ").split())) 

#Tính tích vô hướng của vector a và vector b
res = 0
for i in range(0,len(a)): 
    res = res + a[i]*b[i]
print("Tích vô hướng của vector a và b là:", res)