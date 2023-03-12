list = []
while True:
    number = input('nhập số vào list: ')
    if number == 'stop':
        break
    list.append(int(number))

for i in list:
    assert i%2==0, 'trong list còn chứa só lẻ'
print('all số chẵn')
