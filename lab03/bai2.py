# số hoàn hảo là các số có ước của chính nó tổng lại bằng nó
n = int(input("Nhập n: "))
for i in range(1, n):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)     
