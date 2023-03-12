n = (input('số phần tử muốn nhập là: '))
a = []
for i in range(0,int(n)):
    print(f'phần tử thứ {i+1} là: ',end=' ')
    x = input()
    a.append(x)
ds = a.copy()
ds.sort()
print(f'phan tu lon thu nhi la: {ds[-2]}')
print('vi tri cua phan tu lon thu nhi la: ',a.index(ds[-2]))
d = len(a)
i = 0
maxd = 0
while i<d:
    while a[i]<='0':
        i+=1
        if i==d:
            break
    if i<d:
        max1 = 0
        j = i
        while a[j]>'0':
            max1+=1
            j+=1
            if j==d:
                break
        if max1>maxd:
            maxd=max1
        i=j
    i+=1
print('số dương liên tiếp dài nhất là: ',maxd)
sumd = 0
while i<d:
    while a[i]<='0':
        i+=1
        if i==d:
            break
    if i<d:
        sum1 = 0
        j = i
        while a[j]>'0':
            sum1+=a[j]
            j+=1
            if j==d:
                break
        if sum1>sumd:
            sumd=sum1
            i==j
    i+=1
    
print('Tổng số dương liên tiếp là: ',sumd)
            
