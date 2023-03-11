a=[2,-4,1,9,-3,6,3,-2,6,8]
sum_a=sum(a)
print (f'tổng các phần tử của a là: {sum_a}')
so_duong=0
sum_so_duong=0
for i in range(len(a)):
    if a[i]>0:
        so_duong+=1
        sum_so_duong+=a[i]
print(f'số hạng dương trong a là {so_duong}')
print(f'tổng số hạng dương trong a là {sum_so_duong}')
m=-1
for i in range (len(a)):
    if a[i]<0:
        m = i
        break
if m == -1:
    print("không tìm thấy phần tử âm trong a")
else:
    print("vị trí phần tử âm đầu tiên trong a là:",m)
n = -1
for i in range(len(a)-1, -1, -1):
    if a[i] > 0:
        n = i
        break
if n == -1:
    print("Không tìm thấy phần tử dương trong a")
else:
    print("Vị trí phần tử dương cuối cùng trong a là:", n)
max_a = a[0]
max_n = 0
for i in range(1, len(a)):
    if a[i] > max_a:
        max_a = a[i]
        max_n = i
print("Phần tử lớn nhất trong a là:", max_a)
print("Vị trí phần tử lớn nhất cuối cùng trong a là:", max_n)