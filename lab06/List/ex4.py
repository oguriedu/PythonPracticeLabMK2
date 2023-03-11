list=[]
while 1:
    n=int(input("Nhập phần tử:"))
    if n == 0:
        break
    list.append(n)
print("Danh sách phần tử đã nhập:",list)
a=[1,2,3]
list[4:4]=a
list.extend([1, 2, 3])
list= a + list
print(list)
k = int(input("Nhập vị trí cần xóa(Bắt đầu từ 1):"))
del list[k-1]
print("Danh sách sau khi xóa phần tử thứ:",k)
print(list)
list.sort()
print("Danh sách theo thứ tự tăng dần:",list)
list.sort(reverse=True)
print("Danh sách theo thứ tự giảm dần:",list)
