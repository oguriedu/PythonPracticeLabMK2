n=int(input('Nhập số phần tử trong list:'))
lst=[]
for i in range(n):
    n1=int(input("Nhập các phần tử trong list:"))
    lst.append(n1)
print(lst)
#1
max_lst=-int()
max_lst_2=-int()
vitri=[]
for i in range(n):
    if lst[i]>max_lst:
        max_lst_2=max_lst
        max_lst=lst[i]
        vitri=[i]
    elif lst[i]==max_lst:
        vitri.append(i)
    elif lst[i]>max_lst_2:
        max_lst_2=lst[i]
print('Phần tử lớn thứ nhì trong danh sách:',max_lst_2)
print('Vị trí của phần tử lớn thứ nhì:',vitri)
#2
s=0
s2=0
for i in range(n):
    if lst[i]>0:
        s2+=1
        if s2>s:
            s=s2
        else:
            s2=0
print('Số lượng các số dương liên tiếp nhiều nhất:',s)
#3
s3=0
s4=0
for i in range(n):
    if lst[i]>0:
        s4+=lst[i]
        if s4>s3:
            s3=s4
        else:
            s4=0
print('Số lượng các số dương liên tiếp có tổng lớn nhất:',s3)






