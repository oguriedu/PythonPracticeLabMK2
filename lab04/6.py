num = int(input("Input a number:"))

d=["zero","one","two","three","four","five","six","seven","eight","nine"]

numlist=[] 
while num > 0: numlist.append(num % 10) 
num = num // 10

for i in reversed(numlist): print(d[i], end=" ")