import random
so = [num for num in range(0,201) if num % 5 == 0 and num % 7 == 0]
random_so= random.choice(so)
print("số ngẫu nhiên:", random_so)