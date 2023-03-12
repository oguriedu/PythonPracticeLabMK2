# Viết chương trình nhập vào một danh sách (list) các phần tử là số tự nhiên cho đến khi 
# nhập vào số 0.
lst=[]
while True:
    n=int(input("Nhập số tự nhiên:"))
    if n==0:
        break
    lst.append(n)
print(lst)
# Viết chương trình Python chuyển các phần tử dương của danh sách lên đầu 
# danh sách và in danh sách ra màn hình
print(sorted(lst,reverse=True))
# Chèn một số m (m nhập vào từ bàn phím ) vào đầu danh sách, cuối danh sách 
# và vị trí thứ 5 của danh sách.
m=int(input("Nhập số m:"))
lst.insert(0,m)
lst.append(m)
lst.insert(4,m)
print("chèn m vào đầu danh sách, cuối danh sách, vị trí thứ 5 trong danh sách: ",lst)