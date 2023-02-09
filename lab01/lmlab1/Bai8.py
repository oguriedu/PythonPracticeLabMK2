import math
def find_centroid(x1, y1, x2, y2, x3, y3):
    x = round((x1 + x2 + x3) / 3,2)
    y = round((y1 + y2 + y3) / 3,2)
    return (x,y)

x1, y1 = map(float, input("Nhập tọa độ đỉnh A (x1, y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ đỉnh B (x2, y2): ").split())
x3, y3 = map(float, input("Nhập tọa độ đỉnh C (x3, y3): ").split())

toa_do = find_centroid(x1, y1, x2, y2, x3, y3)

print("Trọng tâm của tam giác là: ", toa_do)
