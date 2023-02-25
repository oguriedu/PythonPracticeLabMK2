sum=0
from tabulate import tabulate 
c={0:20000,1:15000,2:15000,3:5000,4:10000}
a=[['cafe',20000],['cam văt',15000],['nước ép cà rốt',15000],['nước lọc ',5000],['nước dừa',10000]]
b=['name']
print(tabulate(a,headers=b,tablefmt='fancy_grid',showindex='always'))
print("What would you like to drink ?")
while True:
    print("Enter 10 if u wanna stop")
    t=int(input("Please enter the drink code:"))
    if t==10:
        break
    d=c[t]
    sum+=d
print('Total:',sum)

