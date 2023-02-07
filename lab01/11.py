n=int(input('Nhập số lần tung xúc sắc: '))
xacsuat = 1 - (215/216)**n
print('xác suất khi tung n lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 là',round(xacsuat*100,2))