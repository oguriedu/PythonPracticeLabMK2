n=int(input("Nhập số tự nhiên n:"))
nhi_phan= ""
while n>0:
    phan_du = n%2
    nhi_phan = str(phan_du)+nhi_phan
    n= n//2
print("Chuỗi nhị phân tương ứng là:",nhi_phan)