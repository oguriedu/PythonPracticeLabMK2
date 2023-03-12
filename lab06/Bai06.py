import random
a=[]
for i in range(1000):
    b=random.randint(0,99999)
    a.append(b)
print('List ban đầu: ')
print(a)
#___Sử dụng hàm sort
print('List sau khi sắp xếp tăng dần: ')
print(sorted(a))
#___Không sử dụng hàm sort
list=[]
while True:
    list.append(min(a))
    a.remove(min(a))
    if len(list)==1000:
        break
print('List sau khi sắp xếp tăng dần: ')
print(list)

