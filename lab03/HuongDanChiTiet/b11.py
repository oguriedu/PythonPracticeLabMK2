SIN = int(input('Nhập số n = '))
if len(str(SIN)) > 9 or len(str(SIN)) < 8:
    print('Số ', SIN, 'không hợp lệ!')
else:
    so_kiem_tra = SIN % 10  # Số kiểm tra là chữ số cuối cùng
    SIN = SIN//10  # Loại bỏ chữ số cuối cùng của SIN
    s1 = int(0)
    s2 = int(0)
    s = str(SIN)
    L = len(s)
    for i in range(1, L+1):
        if i % 2 != 0:
            s1 += int(s[i-1])
        else:
            tg1 = int(s[i-1])*2  # Các số có vị trí chẵn nhân đôi
            # Nếu kết quả nhân đôi <=9 thì cộng vào s2
            if tg1 <= 9:
                s2 += tg1
            else:  # Nếu kết quả nhân đôi >9 lấy tổng 2 chữ số
                tg2 = tg1//10 + tg1 % 10
                s2 += tg2
    print("số kiểm tra của ", SIN, '=', so_kiem_tra)
    print("Giá trị s1 của", SIN, '= ', s1)
    print("Giá trị S2 của", SIN, '= ', s2)
    trong_so = s1+s2
    if (trong_so + so_kiem_tra) % 10 == 0:
        print('Số ', SIN, 'là số SIN hợp lệ!')
    else:
        print('Số ', SIN, 'là số SIN không hợp lệ!!!')
