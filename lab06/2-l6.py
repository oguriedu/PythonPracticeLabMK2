B=a.copy()
m=max(B)
i=0
while i<len(B):
    if B[i]==m:
        B.remove(B[i])
        i-=1
    i+=1
if len(B)==0:
    print("Khong co so lon nhi")
else:
    m=max(B)
    print("So lon nhi la",m,"tai vi tri",end=" ")
    for i in range(len(a)):
        if a[i]==m:
            print(i+1,end=", ")