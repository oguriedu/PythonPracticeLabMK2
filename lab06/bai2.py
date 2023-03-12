n = int(input('nhập số phần tử trong list:'))
ls = [0]*n
for i in range(n):
    ls[i] = int(input(f'nhập phần tử thứ {i}:'))
print('list vừa nhập:', ls)

ls_n = ls.copy()
ls_n.remove(max(ls_n))
print('giá trị lớn thứ nhì của list là:', max(ls_n))
print('vị trí của các phần tử lớn thứ nhì: ', end='')
for i in range(len(ls)):
    if ls[i] == max(ls_n):
        print(i, end='   ')

max = 0
count = 0
temp1 = 0
temp2 = 0
max_sum = 0
for i in ls:
    if i > 0:
        count += 1
        temp1 += i
        if count > max:
            max = count
        if temp1 > max_sum:
            max_sum = temp1
            temp2 = count
    else:
        count = 0
        temp1 = 0
print('\nsố lượng các số dương liên tiếp nhiều nhất:', max)
print(temp2, 'số liên tiếp có tổng lớn nhất = ', temp1)
