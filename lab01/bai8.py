
def trong_tam_I(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    xI = (x1 + x2 + x3) / 3
    yI = (y1 + y2 + y3) / 3
    zI = (z1 + z2 + z3) / 3
    return xI, yI,zI

x1, y1, z1 = map(float, input("Nhập tọa độ đỉnh A : ").split())
x2, y2, z2 = map(float, input("Nhập tọa độ đỉnh B : ").split())
x3, y3, z3 = map(float, input("Nhập tọa độ đỉnh C : ").split())

xI, yI, zI = trong_tam_I(x1, y1, z1, x2, y2, z2, x3, y3, z3)
print("Tọa độ trọng tâm tam giác:", xI, yI, zI)
