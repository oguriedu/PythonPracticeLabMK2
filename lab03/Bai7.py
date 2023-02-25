#Chương trình tính tổng  nghịch đảo của n số nguyên đầu 
n=int(input('Nhập n = '))
s=0
for i in range(1,n+1):
    s+=1/i
print('S =',s)