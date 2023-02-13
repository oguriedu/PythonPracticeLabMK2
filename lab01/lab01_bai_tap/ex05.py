a, b, c = map(float, input(
    'Nhập giá trị a,b,c của phương trình bậc 2: ').split())
x = -b/(2*a)
y = a*x*x + b*x + c
print(f'Tọa độ đỉnh cần tìm là ({x:.2f},{y:.2f})')
