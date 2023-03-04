str=input('nhập chuỗi ký tự:')
print(f'chuỗi ký tự vừa nhập {str}')
count=0
count1=0

for i in str:
    if '0'<=i<'9':
        count+=1
for i in str:
    if 'a'<=i<='z':
        count1+=1
        count2=len(str)-count-count1

        
print('số ký tự kh phải là chữ cái ta và số là:',count2)       
    