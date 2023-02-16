a = int(input('Nhập một số: '))
sum = 0
for i in range(1, a):
    if a % i == 0:
        sum += i
if sum == a:
    print(a, "là số hoàn hảo")
else:
    print(a, "không là số hoàn hảo")