import random
a=[]
while len(a)<1000:
    a.append(random.randint(1,99999))
print("List A:",a)
a=sorted(a)
print("Sắp xếp theo thứ tự tăng dần:",a)
#khong su dung sorted
n = len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1] , a[j]
print(a)