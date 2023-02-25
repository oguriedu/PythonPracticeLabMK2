while True:
    tu_so=int(input('Nhập giá trị tử số:'))
    mau_so=int(input('Nhập giá trị mẫu số:'))
    if mau_so==0:
        print('Gía trị không hợp lệ, mời bạn nhập lại!')
        continue
    else:
        phan_so=tu_so/mau_so
        break
print(phan_so)