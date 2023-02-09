'v=v0+at'
'gia tốc =-log(4,5)'
'a=v-v0/t-t0''vân tốc sau bằng 0,t0=0'
import math
a=float(input('nhâp vận tốc:'))
van_toc=a**4
gia_toc=-(math.log(5,4))
t=(0-a**4)/(gia_toc)
print('với vận tốc ban đầu là',van_toc,'m/s',',','thời gian ô tô đi cho đến khi dừng là:%0.2f'%t,'s')