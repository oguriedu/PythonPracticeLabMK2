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
list[5:5]=1,2,3
print('add in 5th =', list)
lenght = len(list1)
list1[lenght:lenght]=[1,2,3]
print('add the last =', list1)
list2[0:0]=1,2,3
print('add the first =', list2)
k = int (input('the elements wanna del: '))
list3.pop(k)
print('the list after remove in k location =', list3)
list4.sort()
print('the list after increase : ', list4)
list5.sort(reverse=True)
print(' the list after reduction =', list5)