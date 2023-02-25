n = input('nhập giá trị n: ')
i = 0
while i<128:
    if chr(i) == n:
        print('giá trị ASCII của kí tự', n, '=', i)
        break
    i += 1
else:
    print('không tìm thấy!!!')
