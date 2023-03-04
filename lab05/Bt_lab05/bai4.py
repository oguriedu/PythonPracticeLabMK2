
a=input('Nhập chuỗi thứ 1:')
b=input('Nhập chuỗi thứ 2:')
kq1=''
kq2=''
i=0
j=0
while i< len(a) or j<len(b):
        if i<len(a): 
                kq1+=a[i]
                i+=1
        if j<len(b):
                kq2+=b[j]
                j+=1
print(kq1+kq2)
