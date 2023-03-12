lst = []
lst2=[1,2,3]
while True:
    n = int(input("Hay nhap phan tu vao list:"))
    lst.append(n)
    if n == 0:
        print("Ket thuc nhap ")
        break
print("List can thao tac la:",list)
lst1=lst.copy()
lst1.append(lst2)
lst1.insert(0,lst2)
lst1.insert(0,lst2)
print('lst sau khi chèn vào',lst1)
a=int(input('nhập vị trí muốn xóa phần tử:'))
lst.pop(a)
print(lst)
lst.sort(reverse=True)
print(f'sắp xếp lst giảm dần: {lst}')
lst.sort(reverse=False)
print(f'sắp xếp lst tăng dần: {lst}')