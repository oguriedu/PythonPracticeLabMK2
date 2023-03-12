n = int(input("Enter a number: "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for i in range(n-2)]
print(",".join(str(f) for f in fibonacci[:n]))