a = int(input('Nhập thứ: '))
while (a>=8) and (a<0):    
    a = int(input('Nhập lại thứ: '))
    break
thu = ['monday','tuesday','wednesday','thursday','friday','sartuday','sunday']
a = a-1
print(thu[a])