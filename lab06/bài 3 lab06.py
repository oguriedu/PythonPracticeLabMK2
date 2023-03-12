# nhập ds list
list = []
list1 = []
list2 = []
list3 = []
while True:
    str = int(input('nhập dãy các phần tử: '))
    if str == 0:
        break
    list.append(str)
    list1.append(str)
    list2.append(str)
    list3.append(str)
# chuyển phần tử dương lên đầu ds và in ra
list.sort(reverse=True)
print(list)
# chèn số m vào đầu ds
m = int (input('nhập số m muốn chèn: '))
list1.insert(0, m)
print('ds mới sau khi chèn số m vào đầu ds:', list1)
# chèn số m vào cuối ds
list2.append(m)
print('ds mới sau khi chèn số m vào cuối ds:', list2)
# chèn số m vào vị trí thứ 5
list3.insert(5, m)
print('ds mới sau khi chèn số m vào vị trí thứ 5 của ds:', list3)

    