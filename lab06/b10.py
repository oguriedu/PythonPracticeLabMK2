import random
while True:
    i=random.randint(0,201)
    if i%5==0 and i%7==0:
        break
print("Số ngẫu nhiên chia hết cho 5 và 7 trong khoảng [0,200] là",i)