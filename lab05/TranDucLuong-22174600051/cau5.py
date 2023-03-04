a=input("Nhập chuỗi:")
b=[]
c=[]
sum=0
for i in a :
    if i.isdigit()==True:
        b.append(i)
    elif i.isalpha()==True:
        c.append(i)
b=''.join(b)
b=int(b)
c=''.join(c)
print('Chuỗi số :',b)
print('Chuỗi kí tự:',c)
for t in range(1,b):
    if b%t==0:
        sum+=t
        if sum==b:
            e='là số hoàn hảo'
        else :
            e='ko phải số hoàn hảo'
print(b,e)
