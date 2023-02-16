'''
kiểm tra số nguyên tố và in ra số nguyên tố gần nhất
'''

a = int(input('Nhập n: '))
a1 = 0
for i in range(1,a+1):
    if a % i == 0:
        a1 += 1
if a1 == 2:
   print(a,'là số nguyên tố')
else:
    print(a,'không là số nguyên tố')
    for i in range(1,a+1):
        a1 = 0
        for j in range(1,i+1):
            if i%j==0:
                a1+=1
        if a1==2 :
            max = 2
            if i > max:
                max = i
    print('Số nguyên tố gần n nhất là :',max)