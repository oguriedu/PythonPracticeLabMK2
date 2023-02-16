
n=int(input("Enter interger:"))
list=[]
def shh(n):
    sum=0
    for i in range (1,n):
        if n%i==0:
            sum+=i
    return sum==n
for y in range(1,n):
    if shh(y):
        list.append(y)
print(list)