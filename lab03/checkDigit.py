a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic = dict.fromkeys(a)
temp = 10
for i in a:
    if temp % 11 ==0:
        temp +=1
    dic[i] = temp
    temp += 1

n = input('Nhập số container:')
n = n.upper()
try:
    sum = 0
    for i in range(0,4):
        sum += dic[n[i]]*2**i
    for i in range(4,10):
        sum += int(n[i])*2**i
    print('số kiểm tra của container {} là:{}'.format(n,sum%11))
except:
    print('số container không hợp lệ!!!!')