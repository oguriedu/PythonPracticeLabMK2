import math

def calculate_probability(n):
    probability = 1 - (5/6)**n
    return round(probability, 2)

n = int(input("Nhập số lần tung: "))
ket_qua = calculate_probability(n)
print("Xác suất cả 3 bi xúc sắc ra 6 trong", n, "lần tung là:", ket_qua)
