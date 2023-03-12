n = int(input("Nhập n: "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2]) for i in range(2, n+1)] 
print(*fibonacci, sep=",")