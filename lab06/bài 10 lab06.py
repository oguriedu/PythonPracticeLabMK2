import random
list = [j for j in range(0, 201) if (j%5==0 and j%7==0)]
A = random.choice(list)
print('số ngẫu nhiên chia hết cho 5 và 7 =', A)
