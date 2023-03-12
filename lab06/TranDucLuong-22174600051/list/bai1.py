a=[2,-4,1,9,-3,6,3,-2,6,8]
sum=0
sum1=0
b=[]
for i in a:
    sum+=i
    if i>0:
        b.append(i)
        sum1+=i
print("vị trí phần tử dương cuối cùng trong danh sach a là:",len(a)-1)
print('số hạng dương có trong dãy a là:',len(b))
print("tổng các số hạng dương là:",sum1)        
print('tôrng tất cả các chữ số là:',sum)
print('phần tử lớn nhất của danh sách là:',max(a))
for y in a:
    if y<0:
        print('vị trí số hạng âm đầu tiên là:',a.index(y))
        break
