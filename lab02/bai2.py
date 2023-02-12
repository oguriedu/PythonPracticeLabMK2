# giải phương trình bậc 2 ax^2+bx+c
import math
def pt_bac_2(a,b,c):
      denta= pow(b,2)-4*a*c
      if denta<0:
            print('Phương trình vô nghiệm')
      elif denta>0:
            print('Phương trình có nghiệm là:',(-b+math.sqrt(denta))/(2*a),((-b-math.sqrt(denta))/(2*a)))
      else:
            print('Phương trình có nghiệm kép là:',-b/2*a)
a=int(input('nhập a:'))
b=int(input('nhập b:'))
c=int(input('nhập c:'))
pt_bac_2(a,b,c)