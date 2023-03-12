import random
n = int(input('Số phần tử muốn nhập là: '))
a = []
for i in range(0,n):
    print(f'phần tử thứ {i+1} là: ',end=' ')
    x = int(input())
    a.append(x)
print('list A:',a)
b = [i for i in a if i%3==0 and i%5!=0]
print('list B: ',b)
c = [i*i for i in a]
print('list C: ',c)
d = [i for i in a if i%3==0]
print('list D: ',random.choice(d))
    
    
    