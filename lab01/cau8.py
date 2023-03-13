
# Khai báo các biến và nhập toạ độ của 3 đỉnh
Ax = int(input("Nhập toạ độ x của đỉnh A: ")) 
Ay = int(input("Nhập toạ độ y của đỉnh A: "))

Bx = int(input("Nhập toạ độ x của đỉnh B: "))
By = int(input("Nhập toạ độ y của đỉnh B: "))

Cx = int(input("Nhập toạ độ x của đỉnh C: "))
Cy = int(input("Nhập toạ độ y của đỉnh C: "))

# Tính trọng tâm tam giác
Gx = (Ax + Bx + Cx) / 3 
Gy = (Ay + By + Cy) / 3 

# In ra toạ độ trọng tâm
print("Toạ độ trọng tâm của tam giác là: (%0.2f, %0.2f)" %(Gx, Gy))
print(f"Toạ độ trọng tâm của tam giác là:({Gx:.2f},{Gy:.2f}) ")
