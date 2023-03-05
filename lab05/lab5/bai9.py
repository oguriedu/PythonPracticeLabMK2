a=input("nhập chuỗi ký tự1: ")
a1=input("nhập chuỗi ký tự2: ")
x=""
l=[]
st=0
for i in a:
    try:
        k=a1.index(i)
        x=""
        m=st
        while k<len(a1):
            if a1[k]==a[m]:
                x+=f"{a1[k]}"
                k+=1
                m+=1
            else:
                l.append(x)
                print(x)
                break
        else:
            l.append(x)
        st+=1
    except:
        continue
x=""
st=0
for i in a1:
    try:
        k=a.index(i)
        x=""
        m=st
        while k<len(a):
            if a[k]==a1[m]:
                x+=f"{a[k]}"
                k+=1
                m+=1
            else:
                l.append(x)
                print(x)
                break
        else:
            l.append(x)
        st+=1
    except:
        continue
print(l)
long1=0
long2=0
for i in l:
    long1=len(i)
    if long1>long2:
        long2=long1
for i in l:
    if len(i)==long2:
        print(i)
