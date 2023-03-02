
x = int(input('Nhập số tự nhiên x: '))
y = int(input('Nhập số tự nhiên y: '))
a = x
b = y
while x!=y:
    if x>y:
        x = x-y
    else:
        y = y-x
bcnn = (a*b)/x
print(f'bội chung nhỏ nhất của {a} và {b} là {bcnn}')