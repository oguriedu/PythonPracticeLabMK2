lst = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để kết thúc): "))
    if num == 0:
        break
    lst.append(num)

print("Danh sách đã nhập:", lst)
for i in range(len(lst)):
    if lst[i] > 0:
        lst.insert(0, lst.pop(i))
print("danh sách sau khi đã cho số dương lên đầu là: ",lst)
m=int(input("nhập 1 số m từ bàn phím "))
lst.append(m)
print("list sau khi thêm m vào cuối danh sách là",lst)
lst.insert(0,m)
print("list sau khi đã thêm phần tử vào đầu danh sách là :",lst)
lst.insert(5,m)
print("list sau khi đã thêm phần tử vào vị trí thứ 5 trongdanh sách là :",lst)