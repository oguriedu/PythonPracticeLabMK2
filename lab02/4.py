a=int(input('Nhập số nguyên: '))
if abs(a)<100:
    print('Chữ số hàng trăm của số đó là:',0)
else:
    print('Chữ số hàng trăm của số đó là',abs(a)//100%10)