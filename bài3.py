b=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
while True:
    a=int(input('nhập thứ trong tuần mà bạn muốn: '))
    if 0<a<8: 
        print(a,':',b[a-1])
        break
    
