lst = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break 
    lst.append(num) 
print("Danh sách các số đã nhập:", lst)
#Chèn danh sách [1,2,3] vào vị trí đầu, cuối và thứ 5 của danh sách.
list_new=[1,2,3]
lst=list_new + lst
list_new.extend(lst)
lst = lst[:4] + [1, 2, 3] + lst[4:]
print("Danh sách mới là:", lst)
#Xóa phần tử thứ k (k nhập từ bàn phím) trong danh sách.
k=int(input("Nhập số k: "))
lst.pop(k)
print(lst)
#Sắp xếp danh sách theo thứ tự tăng dần, giảm dần
lst.sort(reverse = True)
print("Thứ tự giảm dần: ",lst)
lst.sort()
print("Thứ tự tăng dần: ",lst)