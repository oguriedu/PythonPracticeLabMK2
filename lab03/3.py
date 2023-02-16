for i in range (2, n): 
    if n % i == 0: print(n,"không phải là số nguyên tố.") 
    break 
else: 
    print(n,"là số nguyên tố.")
    if n < 2: print("Số bé hơn 2, không có số nguyên tố gần n nhất.") 
    else: 
        for i in range(2, n): 
            if n % i == 0: print("Số nguyên tố gần n nhất là:", n-1) 
            break 
        else: 
            print("Số nguyên tố gần n nhất là:", n+1)