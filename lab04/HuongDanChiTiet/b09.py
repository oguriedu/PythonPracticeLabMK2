h = int(input('Nhập vào độ cao/số dòng của tam giác:'))
dong = 1
# Vòng lặp ngoài xác định dòng
while (dong <= h):
    cot = 1
    # vòng lặp trong in giá trị tại vị trí các cột trên từng dòng
    while (cot <= dong):
        print(cot, end=' ')
        cot += 1
    # '\r' xuống dòng và đưa con trỏ về đầu dòng tiếp theo
    print('\r')
    dong += 1
