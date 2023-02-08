thu=int(input("Nhập thứ : "))
while True:
    if (thu>7) or (thu<1):
        print("Nhập lỗi, hãy nhập lại(Nhập từ 1 đến 7)")
        thu=int(input("Nhập thứ : "))
    else:
        break
if thu==1:
    print('today is sunday')
elif thu==2:
    print('today is monday')
elif thu==3:
    print('today is tuesday')
elif thu==4:
    print('today is wednesday')
elif thu==5:
    print('today is thursday')
elif thu==6:
    print('today is friday')
elif thu==7:
    print('today is saturday')
