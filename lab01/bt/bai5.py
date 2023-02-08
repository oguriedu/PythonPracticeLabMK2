
a=input("nhập tọa độ A: ")
b=input("nhập tọa độ B: ")
diem_a=a.split(",")
diem_b=b.split(",")
t=0
for i in range (len(diem_a)):
    t+=int(diem_a[i-1])*int(diem_b[i-1])
print("Tích vô hướng 2 vecto A và B là : ",t)