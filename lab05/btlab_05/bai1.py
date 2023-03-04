str=input('nhập chuỗi ký tự:')
print(f'chuỗi ký tự vừa nhập{str}')
count=0
for i in str:
    if '0' <=i<='9':
        count+=1
print(f'số các ký tự là số trong chuỗi đã nhập là:{count}')
