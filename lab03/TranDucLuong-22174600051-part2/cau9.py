n=int(input('Enter interger:'))
l=[]
l.append(n)
import math
for ch in l:
    if ch<0:
        print("Errol!")
        break 
    else:
        def a(n):
            if n==1:
                return 1
            else :
                return (pow(n,2)+a(n-1))
        print("Answer of a:",a(n))
        def b(n):
            if n==1:
                return 9
            else :
                return ((pow(2*n+1,3)+b(n-1)))
        print('Answer of b :',b(n))
        
        def c(n):
            if n==1:
                return pow(2,4)
            else :
                return (pow(2*n,4)+c(n-1))
        print("Answer of c:",c(n))