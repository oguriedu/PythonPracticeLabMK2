import sys
a = 0
while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    l = s.split(" ")
    operation = l[0]
    amount = int(l[1])
    if operation=="D":
         a+=amount
    elif operation=="W":
        a-=amount
    else:
        pass
print (a)