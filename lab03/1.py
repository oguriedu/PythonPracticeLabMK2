for num in range(1, n):
    sum = 0 
    for i in range(1, num): 
     if num % i == 0: sum = sum + i 
     if sum == num: 
         print(num)