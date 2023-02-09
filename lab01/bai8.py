a1, a2 = map(float,input("Nhập toạ độ điểm A: ").split())
b1, b2 = map(float,input("Nhập toạ độ điểm B: ").split())
c1, c2 = map(float,input("Nhập toạ độ điểm C: ").split())
d = (a1 + b1 + c1)/3
e = (a2 + b2 + c2)/3
print('Trọng tâm của tam giác là: %0.2f'%d, '%0.2f'%e)