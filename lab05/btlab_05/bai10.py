binary = input('nhập dãy nhị phân')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print (f'số thập phân tương ứng là {decimal}')