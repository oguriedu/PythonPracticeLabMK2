num = int(input("Nhập một số nguyên dương: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print("Tổng các chữ số của số vừa nhập là:", sum)
