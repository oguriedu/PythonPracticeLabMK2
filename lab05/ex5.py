chuoi = input('nhập chuỗi kí tự : ')
a=[]
for i in chuoi:
    if i.isdigit()==True:
        a.append(i)
a =''.join(a)
print('chuỗi số:', a)
b = int(a)
def in_shh(b):
    sum = 0
    for i in range(1, b):
        if b%i==0:
            sum += i
    return sum == b
if in_shh(b):
    print('đây là số hoàn hảo !!')
else: 
    print('đây không là số hoàn hảo !!')