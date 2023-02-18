n = int(input("Nhập vào một số nguyên dương: "))

# In ra số 1 không có thừa số nguyên tố
if n == 1:
    print("1 không có thừa số nguyên tố")
else:
    factors = [] # Khởi tạo danh sách chứa các thừa số nguyên tố

    # Phân tích thành các thừa số nguyên tố
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n // i
        else:
            i += 1

    # In ra các thừa số nguyên tố
    print("Các thừa số nguyên tố của số đã cho là:", end=" ")
    for f in factors:
        print(f, end=" ")
