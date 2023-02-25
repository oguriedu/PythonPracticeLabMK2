n = int(input('nhập một số: '))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không là số hoàn hảo")