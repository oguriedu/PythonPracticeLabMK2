tong1 = 0
tong2 = 0
tong3 = 0
n = int(input('Nhập số nguyên dương n: '))
while n<=0:
    n = int(input('Nhập lại n: '))
    break
for i in range(1,n+1):
    tong1 +=i*i
for i in range(1,n+1):    
    if i%2!=0:
        tong2+=i*i*i
    if i%2==0:
        tong3+=i**4
print(tong1)
print(tong2)
print(tong3)
        