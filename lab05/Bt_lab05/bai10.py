str=input('Nhập một chuỗi ký tự nhị phân:')
decimal=0
for i in range(len(str)):
    decimal+=int(str[i])*(2**(len(str)-i-1))
print('Số thập phân tương ứng:',decimal)