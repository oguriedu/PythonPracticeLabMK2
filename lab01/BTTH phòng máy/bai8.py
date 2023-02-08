xa=float(input('Nhập giá trị x của td a:'))
ya=float(input('Nhập giá trị y của td a:'))
print('Tọa độ đỉnh a:',xa,ya)
xb=float(input('Nhập giá trị x của td b:'))
yb=float(input('Nhập giá trị y của td b:'))
print('Tọa độ đỉnh b:',xb,yb)
xc=float(input('Nhập giá trị x của td c:'))
yc=float(input('Nhập giá trị y của td c:'))
print('Tọa độ đỉnh c:',xc,yc)
gx=(xa+xb+xc)/3
gy=(ya+yb+yc)/3
print('Trọng tâm của tam giác là:%0.2f'%gx,gy)
