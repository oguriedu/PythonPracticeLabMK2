a = [2,-4,1,9,-3,6,3,-2,6,8]

print(a)
tong_duong = 0
count = 0
sumA = 0
for i in a:
    sumA += i
    if i > 0:
        count += 1
        tong_duong += i
print('số các số hạng dương:',count)
print('tổng các số hạng dương:',tong_duong)
for i in range(len(a)):
    if a[i] < 0:
        print('vị trí của phần tử âm đầu tiên trong danh sách là:',i)
        break
for i in range(len(a)-1,-1,-1): 
    if a[i] > 0:
        print('vị trí của phần tử dương cuối cùng trong danh sách:',i)
        break

print(f'phần tử lớn nhất trong danh sách là {max(a)} ở vị trí {a.index(max(a))}')