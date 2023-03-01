n = int(input("Nhap n: "))
if (n < 2):
    print("Yeu cau nhap n lon hon 1")
else:
    print("n = ", end="")
    result = ""
    i = 2
    for k in range(n):
        if n % i == 0:
            n //= i
            result = f"{result}x{i}"
        else:
            i += 1
    print(result[1:len(result)])