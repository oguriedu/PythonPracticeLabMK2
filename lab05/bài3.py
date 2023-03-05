#chuyển đổi số tự nhiên n sang số nhị phân 
n=int(input("nhập số tự nhiên n = "))
so_nhi_phan = bin(n)[2:]
print("số n chuyển sang hệ nhị phân là = ",so_nhi_phan)