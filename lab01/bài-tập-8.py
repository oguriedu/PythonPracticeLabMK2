x1, y1 = map(float, input('nhập tọa độ điểm A(x1, y1): ').split())
x2, y2 = map(float, input('nhập tọa độ điểm B(x2, y2): ').split())
x3, y3 = map(float, input('nhập tọa độ điểm C(x3, y3): ').split())

x = round((x1 + x2 + x3)/3,2)
y = round((y1 + y2 + y3)/3,2)

print ('tọa độ trọng tâm tam giác là: ', (x, y))
