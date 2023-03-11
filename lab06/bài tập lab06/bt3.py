lst =[]
while True:
    n=int(input("Nhập số tự nhiên:"))
    if n==0:
        break
    lst.append(n)
print(lst)

print(sorted(lst,reverse=True))

m=int(input("Nhập số m:"))
lst.insert(0,m)
lst.append(m)
lst.insert(4,m)
print("chèn m vào đầu danh sách, cuối danh sách, vị trí thứ 5 trong danh sách: ",lst)