str = input ('nhập chuỗi kí tự nhị phân(chỉ bao gồm các số 0 và 1): ')
number = 0
for i in range(len(str)):
    number += int(str[i])*(2**(len(str)-i-1))
print('số thập phân tương ứng là:', number)