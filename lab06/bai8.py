def Fibonacci(n):
    f0, f1 = 1, 1
    for _ in range(n):
        yield f0
        f0, f1 = f1, f0+f1
fibs = list(Fibonacci(7))
print (fibs)