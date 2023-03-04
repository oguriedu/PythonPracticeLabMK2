n = input("Nhập chuỗi:")
a = []
c = []
sum = 0
for i in n:
    if i.isdigit() == True:
        a.append(i)
    elif i.isalpha() == True:
        c.append(i)
a = ''.join(a)
a = int(a)
c = ''.join(c)
print('Chuỗi số :',a)
print('Chuỗi kí tự:',c)
for t in range(1, a):
    if a % t == 0:
        sum += t
        if sum == a:
            e = 'là số hoàn hảo'
        else :
            e = 'ko phải số hoàn hảo'
print(e)