n = int(input("Nhập n: "))

fibonacci = [0, 1]

while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(",".join(str(x) for x in fibonacci))