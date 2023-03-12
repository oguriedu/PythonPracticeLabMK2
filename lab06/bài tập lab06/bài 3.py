
lst = []
lst1 = []
lst2 = []
lst3 = []
while True:
    str = int(input('enter the elements: '))
    if str == 0:
        break
    lst.append(str)
    lst1.append(str)
    lst2.append(str)
    lst3.append(str)
lst.sort(reverse=True)
print(lst)
m = int (input('enter the elements wanna add: '))
lst1.insert(0, m)
print('new list:', lst1)
list2.append(m)
print('new list 2:', lst2)
list3.insert(5, m)
print('new list after add m in the 5th:', lst3)

    