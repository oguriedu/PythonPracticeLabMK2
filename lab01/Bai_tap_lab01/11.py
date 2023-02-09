a = [int(x) for x in input('Nhập tọa độ đỉnh A: ').split()]
b = [int(x) for x in input('Nhập tọa độ đỉnh B: ').split()]
c = [int(x) for x in input('Nhập tọa độ đỉnh C: ').split()]
x1, y1 = a
x2, y2 = b
x3, y3 = c
x = (x1+x2+x3)/3
y = (y1+y2+y3)/3
print(f'Tọa độ trọng tâm tam giác: ({round(x,2)},{round(y,2)})')
