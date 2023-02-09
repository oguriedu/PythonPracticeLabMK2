#bài 11
n=int(input('Nhập số lần tung xúc sắc: '))
xacsuat = ((1/6)*n)+((1/6)*n)+((1/6)*n)-((1/6)*(1/6))-((1/6)*(1/6))-((1/6)*(1/6))+((1/6)*(1/6)*(1/6))
print('xác suất khi tung n lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 là',round(xacsuat,2),"%")