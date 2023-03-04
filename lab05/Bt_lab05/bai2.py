n=input('Nhập giá trị:')
count=0
for i in n:
    if not i.isalpha() and not i.isnumeric():
        count+=1
print(count) 
