Str=input('Nhập chuỗi: ')
num=""
for c in Str:
    if '0'<=c<='9':
        num+=c
    else :
        if "a" <=c<="z" or "A"<=c<="Z":
            del c
print('Chuối số trong chuỗi là',num)
sum = 0
for i in range(1,int(num)):
    if int(num)%i==0:
        sum+=i
if sum==int(num):
    print(f'{num} là số hoàn hảo') 
else:
    print(f'{num} không là số hoàn hảo')