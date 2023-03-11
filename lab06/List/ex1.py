a=[2,-4,1,9,-3,6,3,-2,6,8]
count = 0
people=[]
print("Tổng các phần tử của danh sách",sum(a))
for i in a:
    if i>0:
       count +=i
       people.append(i)
print("Tổng số hạng dương:",count,"Và số lượng số hạng dương:",len(people))
for b in range(len(a)):
    if a[b]<0:
        print("Vị trí của phần tử âm đầu tiên trong danh sách::",b)
        break
for c in reversed(range(len(a))):
    if a[c]>0:
        print("Vị trí của phần tử dương cuối cùng trong danh sách:",c)
        break
max_value = max(a)
for i in reversed(range(len(a))):
    if a[i] == max_value:
        max_index = i
        break
print("Phần tử lớn nhất cuối cùng của danh sách a là:", max_value, ", ở vị trí:", max_index)