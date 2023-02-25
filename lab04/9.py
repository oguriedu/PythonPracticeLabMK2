n=0
while True:
    i=int(input("Nhập số bất kì:"))
    n+=i
    i=input("Bạn muốn tiếp tục nhập không? Nhấn 0 để dừng nhập:")
    if i=='0':
        break
print('Tổng các chữ số vừa nhập là:',n)