a=[2,-4,1,9,-3,6,3,-2,6,8]
n=10
print(f"Tổng các phần tủ trong danh sách là {sum(a)}")
a1=[]
for i in a:
    if i>0:
        a1.append(i)
print(f"Có {len(a1)} số hạng dương và tổng số hạng dương là {sum(a1)}")
for i in a:
    if i<0:
        print(f"Vị trí phần tử âm đầu tiên trong danh sách là {a.index(i)}")
        break
for i in range(n-1,0,-1):
    if a[i]>0:
        print(f"Vị trí phần từ dương cuối cùng trong danh sách là {a.index(a[i])}")
        break
lst=[]
for i in range(0,n):
    if a[i]==max(a):
        lst.append(i)
print(f"Phần tử lớn nhất trong danh sách là {max(a)}, vị trí của phần tử lớn nhất cuối cùng là {lst[-1]} ")