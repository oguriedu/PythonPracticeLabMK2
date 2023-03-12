
import sys
a = 0
while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    l = s.split(" ")
    o = l[0]
    t = int(l[1])
    if o=="D":
         a+=t
    elif o=="W":
        a-=t
    else:
        pass
print (a)