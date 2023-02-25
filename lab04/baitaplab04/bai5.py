n=int(input('nhập n:'))
while True:
    if n>0:
        print('tiếp tục nhập n')
        n=int(input('nhập tiếp n:'))
    if n<0:
        print('dừng nhập')
    break