
str=input("Nhập một chuỗi ký tự nhị phân: ")
a = True
for char in str:
    if char != '0' and char != '1':
        a=False
        break
if a:
    d=0
    for i in range(len(str)):
        d+=int(str[i])*(2**(len(str)-i-1))
    print("Số thập phân tương ứng là:", d)
else:
    print("Chuỗi ký tự bạn nhập không phải là chuỗi nhị phân.")