str1=input('nhập chuỗi:')
print('chuỗi số vừa nhập là:',str1)
numeric_filter=filter(str.isdigit,str1)
numeric_string="".join(numeric_filter)
print('chuỗi số có trong ',str1,'là',numeric_string)
tong=0
for i in range(1,int(numeric_string)):
    if (int(numeric_string) % i==0):
        tong+=i
if (tong==int(numeric_string)):
    print(numeric_string,'là số hoàn hảo')
else:
    print(numeric_string,'không là số hoàn ')

