n=10
a=[2, -4, 1, 9, -3, 6, 3, -2, 6, 8]
print()
tong=0
tonga=0
dem=0
for i in range(0,n):
    tong+=a[i]
print('tông số các phần tủ trong danh sách:',tong)
for i in range(0,n):
    dem+=1
    tonga+=a[i]>1
print('số lượng các số hạng dương:',tonga)
print('tổng của các số hạng dương:',dem)
