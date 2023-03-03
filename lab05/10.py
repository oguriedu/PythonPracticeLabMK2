str = input("Nhập một chuỗi ký tự nhị phân: ")
binary = True
for char in str:
    if char != '0' and char != '1':
        binary = False
        break
if binary:
    decimal = 0
    for i in range(len(str)):
        decimal += int(str[i]) * (2**(len(str) - i - 1))
    print("Số thập phân tương ứng là:", decimal)
else:
    print("Chuỗi ký tự bạn nhập không phải là chuỗi nhị phân.")
