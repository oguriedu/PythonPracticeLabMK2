n=int(input('Nhập danh sách các phần tử trong list:'))
lst=[]
while n!=0:
    lst.append(n)
    n=int(input('Nhập danh sách các phần tử trong list:'))
print(lst)
#1
a=0
for i in range(len(lst)):
    if lst[i]>0:
        lst[a],lst[i]=lst[i],lst[a]
        a+=1
print('Danh sách list mới:',lst)
#2
n1=int(input('Nhập số cần chèn vào đầu và cuối danh sách:'))
lst.insert(0,n1)
lst.append(n1)
print('List sau khi chèn:',lst)

