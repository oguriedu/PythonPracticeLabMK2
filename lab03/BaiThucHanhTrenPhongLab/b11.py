n = int(input("Nhap n: "))
k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(" ", end="")
    k = k - 1
    for j in range(0, i+1):
        print("* ", end="")
    print("\r")

k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(" ", end="")
    k = k - 1
    if i > 1 and i < n-1:
        for j in range(0, i+1):
            if j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
        print("\r")
    else:
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

k = n - 1
for i in range(0, n):
    for j in range(0, k):
        print(" ", end="")
    k = k - 1
    if i > 1 and i < n-1:
        for j in range(0, i+1):
            if j == 0 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")
        print("\r")
    elif i == n-1:
        for j in range(0, i+1):
            if j == i:
                print("*", end="")
            else:
                print("**", end="")
        print("\r")
    else:
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
