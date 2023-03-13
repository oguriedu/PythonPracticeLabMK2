n=int(input('Nhập số lần tung xúc xắc: '))
#Xác suất tung n lần 1 con xúc xắc có ít nhất 1 lần ra 6
p=1-(5/6)**n
print("Xác suất khi tung n lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 : ",round(p**3,2))