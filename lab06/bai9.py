lst = []
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    x = int(input("Nhập số nguyên: "))
    lst.append(x)

for num in lst:
    assert num % 2 == 0, "Có ít nhất một số không phải là số chẵn trong list."

print("Tất cả các số là số chẵn trong list.") 