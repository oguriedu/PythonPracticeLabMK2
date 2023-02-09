e=['lẻ','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
a=int(input('nhập số: '))
b=a//100
c=(a//10)%10
d=a%10
if c!=0:
    if d!=0: print(e[b],'trăm',e[c],'mươi',e[d])
    else: print(e[b],'trăm',e[c],'mươi')
else:
    if d!=0: print(e[b],'trăm',e[c],e[d])
    else: print(e[b],'trăm')