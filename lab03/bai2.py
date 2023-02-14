n = int(input('Nhập n:'))
def check(n):
    temp = 0
    for i in range(1,n):
        if n % i == 0:
            temp += i
    if temp == n:
        return True
    else:
        return False

print('Các số hoàn hảo nhỏ hơn n:',end=' ')
if n < 6:
    print('không có')
else:
    for i in range(1,n):
        if check(i) == True:
            print(i,end='; ')
        
