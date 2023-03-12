n=int(input('Số phần tử của list: '))
a=[]
while True:
   b=int(input('Nhập phần tử của list: '))
   a.append(b)
   if len(a)==n:
      break
m=0
for i in a:
    if i==max(a):
        continue
    if i>m:
        m=i
print(f'Phần tử lớn thứ nhì trong list: {m}')
a1=a.copy()
vtri=[]
for i in a1:
    if i==m:
        vtri.append(a1.index(i))
        a1[a1.index(i)]=0
print('Các vị trí của phần tử lớn thứ nhì:',vtri)



           