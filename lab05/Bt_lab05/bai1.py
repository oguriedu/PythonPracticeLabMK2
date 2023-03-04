n=input('Nhập giá trị:')
count=0
for i in n:
    if i.isnumeric():
       count+=1
print('Số các ký tự là số là:',count)
