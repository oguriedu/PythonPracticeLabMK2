a=[]
while True:
    a.append(int(input('Nhập phần tử vào list: ')))
    stop=input('ấn phím bất kì để tiếp tục (Nhập e để dừng):  ')
    if stop=='e':
        break
b=a.copy()
b.sort(reverse=True)
for index, value in enumerate(b):
    print("Phần tử {} ở vị trí {}".format(value, index))
    for i in range(0,len(a)):
        if a[i]==b[1]:
            print(i,end=' ')
print()
count=0
max=0
lst=[]
lst1=[]
for i in a:
    if i>0:
        count+=1
        lst.append(i)
    else:
        count=0
        lst1.append(list(lst))
        lst.clear()
    if max<count:
        max=count
print(f"Số lượng phần tử dương liên tiếp là {max}")
for i in lst1:
    if max<sum(i):
        max=sum(i)
        count=len(i)
print(f"Số lượng các số dương liên tiếp có tổng lớn nhất là {count}")
