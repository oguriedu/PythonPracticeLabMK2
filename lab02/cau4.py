a=int(input('Nhập vào 1 số nguyên : '))
if a<100:
    print(f'Chữ số hàng trăm của {a} là :0')
else:
    print('Chữ số hàng trăm của ',a,'là %d'% (a/100%10))
# a=int(input('Nhập số nguyên: '))
# if abs(a)<100:
    # print('Chữ số hàng trăm của số đó là:',0)
# else:
    # print('Chữ số hàng trăm của số đó là',abs(a)//100%10)
a=23432/100
b=a%10
print(a)
print(b)