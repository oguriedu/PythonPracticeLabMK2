def prime_factors(n, factor_list):
    # Lặp từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # Nếu i là số nguyên tố, thêm i vào danh sách thừa số nguyên tố
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                factor_list.append(i)
                # Đệ quy phân tích thừa số nguyên tố của n/i
                prime_factors(n // i, factor_list)
                return factor_list
    # Nếu n không chia hết cho bất kỳ số nguyên tố nào từ 2 đến căn bậc hai của n,
    # nghĩa là n là số nguyên tố, ta thêm n vào danh sách thừa số nguyên tố
    factor_list.append(n)
    return factor_list

# Nhập số nguyên dương
n = int(input("Nhập số nguyên dương: "))

# Phân tích thành thừa số nguyên tố
factors = prime_factors(n, [])

# Xuất kết quả
print(f"Thừa số nguyên tố của {n} là: ", end="")
for factor in factors:
    print(factor, end=" ")