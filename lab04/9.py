sum=0
while True:
    i=int(input('Nhập số ngẫu nhiên: '))
    sum+=i
    i=input('Bạn muốn tiếp tục nhập không? Nhấn 0 để dừng :   ')
    if i=='0':
        break
print('Tổng các chữ số vừa nhập là:',sum)