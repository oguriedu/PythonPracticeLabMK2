n = int(input('Nhập số nguyên dương n: '))
S1 = 0
S2 = 0
S3 = 0
if n<1:
    print('n sai rồi!, hãy nhập lại n')
else:
    for x in range(1,n+1):
        S1+=x
    for y in range(1,n+1,2):
        S2+=y
    for z in range(2,n+1,2):
        S3+=z
    print('S1 =',S1) 
    print('S2 =',S2) 
    print('S3 =',S3) 
