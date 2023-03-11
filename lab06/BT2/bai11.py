listA = []
n = int(input("nhap phan tu : "))

for i in range(0, n):
    print("{}: ".format(i + 1))
 
    listA.append(input())  
print("List=: \n", listA)
ListB=[]
for i in listA:
    if i%3==0 and i%5!=0 :
        ListB.append(i)
print(" ListB= ",ListB)