def fibonacci(n):
    if n == 0:
    
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Nhập vào n: "))
fib_list = [fibonacci(i) for i in range(n+1)]
print(",".join(str(x) for x in fib_list))
