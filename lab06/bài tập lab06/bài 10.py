list = []
while True:
    number = input('enter the elements of list: ')
    if number == 'stop':
        break
    list.append(int(number))

for i in list:
    assert i%2==0, 'list have odd'
print('even number')