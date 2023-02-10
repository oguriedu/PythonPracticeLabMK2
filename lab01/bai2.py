d=int(input('nhập d:'))
h=int(input('nhập h:'))
m=int(input('nhập m:'))
s=int(input('nhập s:'))
def convert(d,h,m,s):
   return  (d*3600*24)+(h*3600)+(m*60)+s
print(convert(d,h,m,s))