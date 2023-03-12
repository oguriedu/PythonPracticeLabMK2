import random
while True:
    d=random.randint(0,201)
    print(d)
    if d%5==0 and d%7==0:
        break
print("Các số ngẫu nhiên chia hết cho 5 và 7 trong khoảng phạm vi [0,200] là",d)