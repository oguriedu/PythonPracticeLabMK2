x1, y1 = map(float, input('Xin mời nhập tọa độ của A: ').split())
x2, y2 = map(float, input('Xin mời nhập tọa độ của B: ').split())
x3, y3 = map(float, input('Xin mời nhập tọa độ của C: ').split())
x4 = (x1 + x2 + x3)/3
y4 = (y1 + y2 + y3)/3
print(f'Tọa độ G cần tìm là ({x4:.2f},{y4:.2f})')
