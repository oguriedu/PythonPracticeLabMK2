lst=[]
while True:
   x=int(input("Nhập giá trị : "))
   if x==0:
      break
   lst.append(x)
print("lst vừa nhập : ",lst)
#tìm phần tử lớn thứ nhì của danh sách
lst1=lst.copy()
lst.sort()
sum=0
for i in lst:
   if(i==lst[-1]):
      sum+=1
      print("Phần tử lớn thứ nhì là:",lst[-sum-1])
      #tìm vị trí các phần tử lứn thứ nhì
print("các vị trí của phần tử đạt giá trị lớn nhì là : ", end=" ")
for i in range(len(lst)):
   if(lst1[i]==lst[-sum-1]):
      print(i,end=' ')
#số lượng các số dương liên tiếp nhiều nhất
x=len(lst)
i=0
maxd=0
while i<x:
    while lst[i]<=0:
      i+=1
      if i==x:
         break
    if i<x:
      max1=0
      j=i
      while lst[j]>0:
         max1+=1
         j+=1
         if j==x:
            break
      if max1>maxd:
         maxd=max1
      i=j
    i+=1
print("số dương liên tiêp dài nhất = ", maxd)
#số lượng các số dương liên tiếp có tổng lớn nhất 
x=len(lst)
i=0
sumd=0
while i<x:
    while x[i]<=0:
        i+=1
        if i==x:break
    if i<x:
        sum1=0
        j=i
        while x[j]>0:
            sum1+=x[j]
            j+=1
            if j==x: break
        if sum1>sumd: 
            sumd=sum1
        i=j
    i+=1
print('Tổng số lượng các số dương liên tiếp có tổng lớn nhất =',sumd)
   