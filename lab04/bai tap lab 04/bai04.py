tử_số=int(input('nhập vào tử số :'))
mẫu_số=int(input('nhập vào mẫu số :'))
if mẫu_số <= 0:
    print('bạn đã nhập mẫu số bằng 0 , xin nhập lại giá trị :')
    mẫu_số=int(input('nhập vào mẫu số :'))

while True:
    phân_số=((tử_số/mẫu_số))
    print((phân_số))
    break
