n=int(input('n: '))

for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i+1):
        if i == n-1 or j == 0 or j == 2*i:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(1, n+1):
    for j in range(1, n+1-i):
        print(" ", end=" ")
    for k in range(1, 2*i):
        if k == 1 or k == 2*i-1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


for i in range(1, n+1):
    for j in range(1, n+1-i):
        print("", end = " ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()