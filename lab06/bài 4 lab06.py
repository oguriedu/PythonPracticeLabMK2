list = []
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
while True:
    number = int(input('nhập phần tử số: '))
    if number == 0:
        break
    list.append(number)
    list1.append(number)
    list2.append(number)
    list3.append(number)
    list4.append(number)
    list5.append(number)
# chèn ds [1,2,3] vào vị trí thứ 5 của ds ban đầu
list[5:5]=1,2,3
print('kq chèn vào vt số 5 =', list)
# chèn ds [1,2,3] vào vị trí cuối cùng của ds ban đầu
lenght = len(list1)
list1[lenght:lenght]=[1,2,3]
print('kq chèn vào vt cuối =', list1)
# chèn ds [1,2,3] vào vị trí đầu tiên của ds ban đầu
list2[0:0]=1,2,3
print('kq chèn vào vt đầu =', list2)
# xóa phần tử thứ k trong ds
k = int (input('nhập phần tử thứ k muốn xóa: '))
list3.pop(k)
print('ds sau khi xóa phần tử thứ k =', list3)
# sắp xếp ds tăng dần gt
list4.sort()
print('ds sau khi xếp tăng: ', list4)
# sắp xếp ds giảm dần gt
list5.sort(reverse=True)
print('ds sau khi xếp giảm =', list5)