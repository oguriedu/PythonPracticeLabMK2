sum = int(0)
for i in range(1000, 3001):
    if i % 3 == 0 and i % 5 != 0:
        sum += i
print("Trong khoảng đóng [1000,3000]", end='')
print("tổng các số là bội của 3 nhưng không chia hết cho 7 =", sum)
