a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
print('Danh sách:',a)
#yc1
print('Tổng các phần tử của danh sách:',sum(a))
#yc2
tong = 0
dem = 0
print('Các số hạng dương:')
for i in range (len(a)):
    num = a[i]
    if num>0:
        print(num,end=',')
        dem+=1
        tong+=num
print('\nSố lượng các số hạng dương:',dem)
print('Tổng các số hạng dương =',tong)
#yc3
for i in range(len(a)):
    if a[i]<0:
        print('Vị trí của phần tử âm đầu tiên trong danh sách:', i+1)
        break
#yc4
for i in range(len(a)):
    if a[i]>0:
        i+=1
print('Vị trí của phần tử dương cuối cùng trong danh sách:',i)
#yc5
max_a = max(a)
last = 1
for i in range(len(a)):
    if a[i] == max_a:
        last+= i
print('Phần tử lớn nhất là', max_a,'ở vị trí thứ',last,'trong danh sách')
