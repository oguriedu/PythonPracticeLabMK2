list = []
while True:
    n = int(input("hãy nhập phần tử vào list:"))
    list.append(n)
    if n == 0:
        print("kết thúc nhập ")
        break
print("List cần thao tác:",list)

listcl = list.copy()
listcl.sort(reverse=True)
print("List sau khi sắp xếp là:",listcl)

m = int(input("Hãy nhập số bạn cần chèn list:"))
list.append(m)
list.insert(0, m)
list.insert(5, m)
print(list)