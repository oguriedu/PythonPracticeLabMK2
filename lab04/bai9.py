S=0
while True:
    a=int(input('Nhập a :'))
    S+=a
    tt=input('Bạn có tiếp tục nhập ko(nhấn 0 để dừng lại)')
    if tt=='0':
        break
    
print(f"Tổng các số vừa nhập là {S}")