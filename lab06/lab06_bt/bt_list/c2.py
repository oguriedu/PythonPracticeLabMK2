n=int(input("Nhập n: "))
lst=[]
s=0
a=0
lt=[]
sum1=0
sum2=0
count=0
for i in range(n):
    i=int(input("Nhập phần tử trong list: "))
    lst.append(i)
lst1=lst.copy()
lst1.remove(max(lst))
print('Phần tử thứ nhì là:',max(lst1))
for i in range (len(lst)):
    if lst[i] == max(lst1):
        print('Vị trí của phần tử thứ nhì là:',i)
while a<len(lst):
    while lst[a]<=0:
        a+=1
        if a==len(lst):
            break
    if a<len(lst):
        lt1=[]
        j=a
        while lst[a]>0:
                lt1.append(lst[a])
                j+=1
                if j==len(lst):
                     break
        if len(lt1)>len(lt):
             lt==lt1.copy
        a=j    
    a+=1


             
print("Dãy số dương liên tiếp=",lt)
print("tổng số lượng các số dương liên tiếp có tổng lớn nhất= ",lt1)
