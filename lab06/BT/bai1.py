a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
tong = 0
dem = 0
tong2 = 0
for i in a:
    tong+=i
print(f'tổng các phần tử trong danh sách là: {tong}')
for i in (a):
    if 1<=i<=9:
        dem+=1
        tong2+=i
print(f'số lượng các số hạng dương: {dem}')
print(f'tổng các số hạng dương là: {tong2}')
print('vị trí của phần tử âm đầu tiên trong danh sách là: ',a.index(-4))
print('Vị trí phần tử dương cuối cùng trong danh sách là: ',a.index(8))
print(f'phần tử lớn  nhất trong danh sách là: {max(a)}')
print(f'vị trí của phần tử lớn nhất là: {a.index(max(a))}')

