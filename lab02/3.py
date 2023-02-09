#3
x = int(input('Nhập thứ: '))
while (x>=8) and (x<0):    
    x = int(input('Thứ không hợp lệ: '))
    break
thu = ['1:sunday','2:monday','3:tuesday','4:wednesday','5:thursday','6:friday','7:sartuday']
x = x-1
print(thu[x])