import random
n = int(input("enter the number of elements of list A: "))
lst_A = [];lst_B = [];lst_C = [];lst_D = [];lst_div3 = []
for i in range(n):
    a = int(input())
    lst_A.append(a)
#choice 1 random num
print("elements of list A is: ",lst_A)
num = random.randint(0,n)
for i in lst_A:
    if i % 3 == 0 and i % 5 != 0:
        lst_B.append(i)
    lst_C.append(i*i)
    if i % 3 == 0:
        lst_div3.append(i)
print("random num is: ",num)
#choose "num" random number div 3 in lst_A
for i in range(num):
    randNum = random.choice(lst_div3)
    lst_D.append(randNum)
print("elements of list B is: ",lst_B)
print("elements of list C is: ",lst_C)
print("elements of list D is: ",lst_D)