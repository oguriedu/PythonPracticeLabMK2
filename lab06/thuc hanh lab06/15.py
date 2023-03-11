lst=[]
while True:
    name=input()
    age=int(input())
    score=int(input())
    lst.append((name,age,score))
    if input('Nhấn q để dừng nhập')=='q':
        break
lst = sorted(lst, key=lambda x: (x[0], x[1], x[2]))
print(lst)