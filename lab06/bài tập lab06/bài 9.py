lst = []
while True:
    number = input('enter the elements of list: ')
    if number == 'stop':
        break
    lst.append(int(number))

for i in lst:
    assert i%2==0, 'in list have odd'
print('even number')