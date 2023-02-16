n = int(input("nhập vào số n : "))
if n > 1:
	for i in range(1,n):
		if n % i == 0:
			print(n, " là số nguyên tố")           
elif n % n !=0 :
	        print(n, "là số nguyên tố")