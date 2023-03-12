n=int(input('Nhập danh sách các phần tử trong list:'))
lst=[]
while n!=0:
    lst.append(n)
    n=int(input('Nhập danh sách các phần tử trong list:'))
print(lst)
#1
z=[1,2,3]
lst=[1,2,3]+lst
lst=lst+[1,2,3]
lst.insert(4,z)
print('List sau khi chèn:',lst)
#2
k=int(input('Nhập phần tử bạn muốn xóa:'))
del lst[k]
print('List sau khi xóa:',lst)
#3
lst.sort()
print('Danh sách list theo thứ tự tăng dần:',lst)
lst.sort(reverse=True)
print('Danh sách list theo thứ tự giảm dần:',lst)
