n = int(input("Nhập giá trị của n: "))
sum = 0
product = 1

for i in range(n):
    product = 1+2/3+2/3 * 4/5 +2/3*4/5 * 6/7 + ... +(2/3)*(4/5)*(6/7)*(8/9)* ... *((2 * (i+1) ) / (2 * i + 3))
    sum += product

print(round(sum, 3))
