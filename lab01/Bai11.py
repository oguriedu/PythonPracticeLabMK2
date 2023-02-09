n=int(input('Nhập số lần tung xúc xắc: '))
p=0
for i in range(1,n+1):
   p+=1/216
print("Xác suất khi tung n lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 : %0.2f"%p)