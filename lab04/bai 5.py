while True:
    number = int(input('Nhập một số: '))
    print(f'Số bạn vừa nhập là: {number}')
    if number < 0:
        break
    else:
        continue
print('Bạn đã nhập số âm, chương trình sẽ dừng lại.')
