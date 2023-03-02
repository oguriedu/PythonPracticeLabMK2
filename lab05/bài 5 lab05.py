chuoi = input('nhập chuỗi kí tự: ')
a=[]
for i in chuoi:
    if i.isdigit()==True:
        a.append(i)
a =''.join(a)
print('chuỗi số:', a)
c = int(a)
def in_shh(c):
    sum = 0
    for i in range(1, c):
        if c%i==0:
            sum += i
    return sum == c
if in_shh(c):
    print('đây là số hoàn hảo!!')
else: 
    print('đây không là số hoàn hảo!!')



