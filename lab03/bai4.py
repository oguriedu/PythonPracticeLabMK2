n=int(input("nhập n :"))
def print_prime_numbers(n):
    # Tạo một mảng chứa các số từ 2 đến n và gán tất cả giá trị là True
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
        # Nếu prime[p] là True, đánh dấu tất cả các bội số của p là False
        if prime[p] == True:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    # In ra các số nguyên tố
    for p in range(2, n+1):
        if prime[p]:
            print(p)
print_prime_numbers(n)