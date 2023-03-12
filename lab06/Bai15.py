lst=[]
while True:
    name=input('Name: ')
    age=int(input('Age: '))
    score=int(input('Score: '))
    lst.append((name,age,score))
    tt=int(input('Bạn có muốn nhập tiếp không ? 0:không; bất kì: có'))
    if tt==0:
        break
lst = sorted(lst, key=lambda x: (x[0], x[1], x[2]))
print(lst)