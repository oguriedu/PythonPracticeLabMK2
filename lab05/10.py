a = input("Nhập một chuỗi ký tự nhị phân: ")
b = True
for i in a:
    if i != '0' and i != '1':
        b = False
        break
if b:
    d = 0
    for j in range(len(a)):
        d += int(a[i]) * (2**(len(a) - i - 1))
    print("Số thập phân tương ứng là:", d)
else:
    print("Chuỗi ký tự bạn nhập không phải là chuỗi nhị phân.")
