a=[2,-4,1,9,-3,-2,6,8]
#1
tong=sum(a)
print('Tổng các phần tử:',tong)
#2
count=0
s=0
for i in range(len(a)):
    if a[i]>0:
        count+=1
        s+=a[i]
print('Số lượng các số hạng dương:',count)
print('Tổng các số dương:',s)
#3
for i in range(len(a)):
    if a[i]<0:
        so_am_dt=i
        break
print('Vị trí phần tử âm đầu tiên trong danh sách:',so_am_dt)
#4
for i in range((len(a)-1),-1,-1):
    if a[i]>0:
        so_duong_cc=i
        break
print('vị trí phần tử dương cuối cùng trong danh sách:',so_duong_cc)
#5
max_a=max(a)
print('Phần tử lớn nhất trong danh sách:',max_a)
vi_tri_max_a=len(a)-a[::-1].index(max_a)-1
print('Vị trí phần tử lớn nhất cuối cùng:',vi_tri_max_a)    