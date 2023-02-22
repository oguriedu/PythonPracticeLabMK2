a = float(input('nhập vào tử số:'))
b = 0
while b == 0: 
    b = float(input('nhập vào mẫu số:'))
    if b == 0:
        print(' error mời nhập lại mẫu số')
print('số vừa nhập có giá trị:',a/b)