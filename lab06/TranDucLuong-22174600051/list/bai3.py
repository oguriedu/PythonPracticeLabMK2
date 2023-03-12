list=[]
while True:
    a=int(input("nhap so:"))
    if a==0:
        break
    list.append(a)
list.sort(reverse=True)
print(list)
m=int(input('nhap so m:'))
list.insert(5,m)
list.append(m)
list.insert(0,m)
print(list)