import random

lst = [random.randint(0, 200) for _ in range(10)]
result = [num for num in lst if num % 5 == 0 and num % 7 == 0]

print(result)
