n=int(input("mời nhập số tự nhiên n: "))
danh_sach=[]
#nhập danh sách
while n!=0:
    danh_sach.append(n)
    n=int(input("mời nhập số tự nhiên n: "))
    if n==0:
        danh_sach.append(n)
        break
#k nhập từ bàn phím
k=int(input("mời nhập k: "))
xoa=danh_sach.copy()
del(xoa[k])
print(f" danh sách sau khi xóa: {xoa}")
#sắp xếp danh sách theo thứ tự tăng dần
danh_sach.sort()
print(danh_sach," danh sách theo thứ tự tăng dần")
danh_sach.reverse()
print(danh_sach," danh sách theo thứ tự giảm dần")
#chèn danh sách [1,3,5]
danh_sach.insert(4,[1,2,3])
danh_sach.insert(0,[1,2,3])
danh_sach.append([1,2,3])
print(f"{danh_sach},là danh sách sau khi chèn")
