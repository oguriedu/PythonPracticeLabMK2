list=[]
while 1:
    n=int(input("Nhập phần tử:"))
    if n == 0:
        break
    list.append(n)
print("Danh sách phần tử đã nhập:",list)
i = 0
j = len(list) - 1
while i < j:
    if list[i] < 0:
        list[i], list[j] = list[j], list[i]
        j -= 1
    else:
        i += 1
print("Danh sách sau khi chuyển các phần tử dương lên đầu:")
print(list)
m=int(input("Nhập tham số:"))
list.insert(0,m)
list.insert(5,m)
list.append(m)
print("Danh sách phần tử sau khi nhập tham số m:",list)