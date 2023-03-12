#đề xuất số ngẫu nhiên kèm điều kiện
import random
so = [num for num in range(0,201) if num % 5 == 0 and num % 7 == 0]
random_num = random.choice(so)

print("số ngẫu nhiên đó là:", random_num)