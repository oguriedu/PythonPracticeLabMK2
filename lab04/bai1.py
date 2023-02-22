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
s1 = 0
s2 = 0
s3 = 0
while i <= n:
    s1 += i**2
    s2 += (2*i+1)**3
    s3 += (2*i)**4
    i +=1
print(s1,s2,s3,sep='\n')

