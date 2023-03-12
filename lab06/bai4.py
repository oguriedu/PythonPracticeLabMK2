lst=[]
lst1=[1,2,3]
while True:
    n=int(input("Nhập số tự nhiên:"))
    if n==0:
        break
    lst.append(n)
print(lst)
# Sắp xếp danh sách theo thứ tự tăng dần, giảm dần.
lst2=sorted(lst)
lst3=sorted(lst,reverse=True)
# Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách.
lst.insert(0,lst1)
lst.append(lst1)
lst.insert(4,lst1)
# Xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.
k=int(input("Nhập phần tử k:"))
lst4=lst.pop(k)

print("chèn [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách",lst)
print("tăng dần",lst2)
print("giảm dần",lst3)
print("xóa phần tử thứ",k,"trong danh sách là phần tử:",lst4)