n = int(input("Nhập vào một số nguyên dương: "))
m = n
result = []
for i in range(2, n + 1):
    if n % i == 0:
        result.append(i)
        n //= i
    if n == 1:
        break
if len(result)==0 or result[-1]!=m:
    result.append(n)
if result[-1]==1:
    del result[-1]
print(f"{m} = {' x '.join(map(str, result))}")
