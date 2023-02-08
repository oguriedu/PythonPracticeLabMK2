import math


v=float(input('Vạn tốc của ô tô:'))
#Vận tốc chậm dần đều v0=-at
t=v/(-v**4+math.log(5,4))
print('Thời gian ô tô đi được cho đến lúc dừng là:%0.2f'%t)
