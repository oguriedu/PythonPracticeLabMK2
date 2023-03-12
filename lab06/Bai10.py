import random
while True:
    i=random.randint(0,200)
    if i%5==0 and i%7==0:
        break
print(f'Số ngẫu nhiên chia hết cho 5 và 7 từ 0 đến 200 là {i}')
