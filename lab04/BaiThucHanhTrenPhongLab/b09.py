while True:
    n = input("Nhap mot so: ")
    if (n.isnumeric()):
        break
sum = 0
for i in n:
    sum = sum + int(i)
print(sum)
