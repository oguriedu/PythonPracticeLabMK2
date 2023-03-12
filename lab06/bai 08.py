n = int(input('Nhập giá trị n: '))
fib = [0, 1]
[fib.append(fib[i-1] + fib[i-2]) for i in range(2, n+1)]
print(*fib, sep=',')
