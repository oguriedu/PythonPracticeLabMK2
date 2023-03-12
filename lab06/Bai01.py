a=[2,-4,1,9,-3,6,3,-2,6,8]
s=0
for i in a:
    s+=i
print(f'Tổng các phần tử trong list: {s}')
duong=[i for i in a if i>0]
print(f'Số phần tử dương trong list: {len(duong)}')
print(f'Tổng các phần tử dương trong list: {sum(duong)}')
for i in a:
    if i<0:
        print(f'Vị trí phần tử âm đầu tiên trong list: {a.index(i)}')
        break
for i in a:
    if i>0:
        b=a.index(i)
print(f'Vị trí phần tử dương cuối cùng trong list: {b}')
print(f'Phần tử lớn nhất trong list: {max(a)}')
for i in a:
    if i==max(a):
        c=a.index(i)
print(f'Vị trí phần tử lớn nhất cuối cùng trong list: {c}')
      
