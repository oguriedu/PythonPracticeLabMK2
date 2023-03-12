import random
lst=[]
for i in range(10):
    lst.append(random.randint(1,99999))
print(lst)
#1
lst.sort()
print('Danh sách list theo thứ tự tăng dần:',lst)
#2
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            a=lst[i]
            lst[i]=lst[j]
            lst[j]=a
print('Danh sách list theo thứ tự tăng dần:',lst)