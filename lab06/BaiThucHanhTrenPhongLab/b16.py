x = int(input("Nhập giá trị X: "))
y = int(input("Nhập giá trị Y: "))

lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)
