n = int(input("Nhap n: "))
sum = 1
multiple = 1
for i in range(n+1):
    multiple = multiple*(2*(i+1)/(2*i+3))
    sum = sum+multiple

print(sum)
