list=[]
list2=[]
import random
for i in range(1,1001):
    list.append(random.randint(1,999999))
list1=list.copy()
list.sort()
print('Sap xep dung ham sort:',list)
for x in range(len(list1)):
    for y in range(len(list1)-x-1):
        if list1[y] > list1[y+1]:
            list1[y], list1[y+1] = list1[y+1], list1[y]
print('ko su dung ham sort:',list1)