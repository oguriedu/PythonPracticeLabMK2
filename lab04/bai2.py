while True:
    try:
        n = int(input('nhập n là số nguyên dương:'))
        if n <=0:
            print('mời bạn nhập lại!!!')
            continue
        else:
            break
    except:
        print('mời bạn nhập lại!!!')

i = 1
s4 = 0
s5 = 0
s6 = 0
while i<=n:
    s4 += 1/i*(-1)**(i+1)
    s5 += 1/(i*(i+1))
    s6 += 1/(i+1)**(1/2)
    i +=1
print(s4,s5,s6,sep='\n')
