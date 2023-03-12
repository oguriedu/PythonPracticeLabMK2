#cau1.a
a=[2,-4,1,9,-3,6,3,-2,6,8]
sum=0
sum1=0

for i in a:
    sum+=i
print(sum)

#cau1.b
b=[x for x in a if x>0]
print(len(b))
for i in b:
    sum1+=i
print(sum1)

#cau1.c
for i in a:
    if i<0:
        print(i)
        break

#cau1.d
def dao():
    a.reverse()
    for i in a:
        if i>0:
            print(i)
            break
dao()

#cau1.e
for i in a:
    if i >=9 :
        print(i)
    