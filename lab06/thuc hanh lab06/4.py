list = []
list2 = [1,2,3]
while True:
    n = int(input("Hay nhap phan tu vao list:"))
    list.append(n)
    if n == 0:
        print("Ket thuc nhap ")
        break
print("List can thao tac la:",list)

listcl = list.copy()
listcl.append(list2)
listcl.insert(0, list2)
listcl.insert(5, list2)
print("List sau khi chen vao la:", listcl)

k = int(input("Nhap vi tri ban muon xoa phan tu:"))
list.pop(k)
print(list)

list.sort(reverse=True)
print("List sau khi sap xep giam dan:",list)
list.sort(reverse=False)
print("List sau khi sap xep tang dan:",list)
