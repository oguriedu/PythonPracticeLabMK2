a=int(input("nhập a: "))
b=int(input("nhập b: "))
if a>=b:
     c=a
else :
     c=b
if (a==b)or(a%b==0)or(b%a==0):
     print(c,"là bội chung nhỏ nhất")
while (c%a!=0)or(c%b!=0):
     c+=1
     if (c%a==0)and(c%b==0):
         print(c,"là bội chung nhỏ nhất")
         break
