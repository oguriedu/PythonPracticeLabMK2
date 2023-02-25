def decimalToString(num):

 result = ""

 while num > 0: remainder = num % 10

 result += chr(remainder + 48)

 num //= 10

 return result[::-1]

 num = int(input("Nhập số thập phân: "))

print(decimalToString(num))