n=int(input("Số lần xúc sắc là: "))
p=(6**3)**n
s=float((6**3-1)**n/p)
print("xác suất khi tung",n,"lần 3 xúc sắc có ít nhất 1 lần cả 3 ra 6 là: ",round(1-s,2))