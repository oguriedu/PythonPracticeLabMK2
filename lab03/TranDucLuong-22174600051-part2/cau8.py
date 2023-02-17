n=int(input('Enter interger:'))
l=[]
l.append(n)
for ch in l:
    if ch<0:
        print("Errol!")
        break 
    else:
        def a(n):
            if n==1:
                return 1 
            else: 
                return(n+a(n-1))
        print('Answer of a:',a(n))

        def c(n):
            if n==1:
                return 2
            else :
                return (2*n+c(n-1))
        print ('Answer of c:',c(n))    

        def b(n):
            if n==1:
                return 3
            else:
                return((2*n+1)+b(n-1))
        print('Answer of b:',b(n))