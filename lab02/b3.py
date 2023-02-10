n = int(input('Nhập thứ: '))
while (n>=8) and (n<0):    
    n = int(input('Nhập lại thứ: '))
    break
thu = ['monday','tuesday','wednesday','thursday','friday','sartuday','sunday']
n = n-1
print(thu[n]) 