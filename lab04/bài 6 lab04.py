number = {'0': 'không', '1': 'một', '2': 'hai', '3': 'ba', '4': 'bốn', '5': 'năm', '6': 'sáu', '7': 'bảy', '8': 'tám', '9': 'chín'}
while True:
    num = str (input('nhập số từ bàn phím: '))
    if num == 'stop':
        break
    i = ' '
    for j in num:
        i += number[j]+ ' '
    print (i.strip())
