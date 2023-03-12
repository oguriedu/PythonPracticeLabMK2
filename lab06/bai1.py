a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
x=0
y=0
print("tổng các phan tu trong list : ",sum(a))

for i in a:
    if i >=0:
        x+=1
        y+=i
print('Tổng = ',y)
print('Số phần tử dương : ',x)
 
for i in a:
    if i<0:
        print("Vị trí số âm đầu tiên : ",a.index(i))
        break
    