tong1 = 1
tong2 = 1
tong3 = 1
n = int(input('Nhập số nguyên dương: '))
while n<=0:
    n = int(input('Nhập lại n: '))
    break
for i in range(1,n+1):
    tong1 =i*(i+1)/2    
    if i%2!=0:
        tong2 = (i+1)*2
    elif i%2==0:
        tong3 = i*(i+1) 
print(tong1)
print(tong2)
print(tong3)
    