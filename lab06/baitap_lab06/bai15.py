lst=[]
while True:
    name=input('nhập tên ')
    age=int(input('nhập tuổi '))
    score=int(input('nhập điểm '))
    lst.append((name,age,score))
    if input('Nhấn q để dừng nhập')=='q':
        break
lst = sorted(lst, key=lambda x: (x[0], x[1], x[2]))
print(lst)