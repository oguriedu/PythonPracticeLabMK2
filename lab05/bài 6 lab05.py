str = input('nhập chuỗi kí tự: ')
def hex_str(str):
    hex = set('0123456789ABCDEF')
    for i in str:
        if i not in hex:
            return False
    return True
if hex_str(str) == False:
    print('đây không là chuỗi hex!!')
    list = []
    for j in str:
        if (j >= 'A' and j <= 'F') or (j >= '0' and j <= '9'):
            list.append(j)
    list = ''.join(list)
    number = int(list, 16)
    print('hệ thập phân =', number)
else:
    print('đây là chuỗi hex!!')
    number = int(str, 16)
    print('hệ thập phân =', number)
