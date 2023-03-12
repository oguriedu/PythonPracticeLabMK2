import random
while True:
    i = random.randint(0,200)
    if i % 5 == 0 and i % 7 ==0:
        break
print('số chia hết cho 5 và 7 là:',i)