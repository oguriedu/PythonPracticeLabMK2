n = int(input("Hay nhap so phan tu trong list:"))
list = []
listcl = []
listyan = []
listsum = []
sum = 0
z = 0


while len(list) < n:
    x = int(input("Hay nhap phan tu trong list:"))
    list.append(x)
    listcl = list.copy()
print("List can thao tac la:",list)

listcl.sort(reverse=True)
y = listcl[1]
print("Phan tu co gia tri lon thu 2 la:",y)
for i in range(0,len(list)):
    if list[i]==listcl[1]:
        print("Vi tri cua no la:", list.index(y),", ",i)
