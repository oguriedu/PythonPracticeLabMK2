a= int(input("Nhập một số:"))
fibonacci = [0, 1]
while len(fibonacci) < a:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(",".join(str(x) for x in fibonacci))