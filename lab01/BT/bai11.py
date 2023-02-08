import random
t=0
while True:
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    if a==b==c==6:
        break
    t+=1
print(round(1/t,3),round((1/6)**3,3),t)