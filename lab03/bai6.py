while True:
    n = int(input('Nhập số nguyên n:'))
    if n > 0:
        break 
sum = 0
for i in range(n+1):
    sum += i**3
print(sum)
