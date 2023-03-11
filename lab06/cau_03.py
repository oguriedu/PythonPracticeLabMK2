list = []
while True:
    n = int(input("Hay nhap phan tu vao list:"))
    list.append(n)
    if n == 0:
        print("Ket thuc nhap ")
        break
print("List can thao tac la:",list)

listcl = list.copy()
listcl.sort(reverse=True)
print("List sau khi sap xep la:",listcl)

m = int(input("Hay nhap so ban can chen vao list:"))
list.append(m)
list.insert(0, m)
list.insert(5, m)
print(list)