#a
n = int(input("Nhập số làm số hàng của tam giác: "))
for i in range(0, n):
    for j in range(0, i+1):
        print("* ", end="")
        print()

#b
n = int(input("Nhập số làm số hàng của tam giác: "))

for i in range(1, n+1):
    
    for j in range(1, n-i+1): print(" ", end="")

for k in range(1, 2*i):
    print("*", end="")

print()

#c
n = int(input("Nhập số làm số hàng của tam giác: ")) 
for i in range(n): 
    for j in range(n-i-1): print(end=" ") 
    for k in range(i+1): print(end=" * ") 
    print()