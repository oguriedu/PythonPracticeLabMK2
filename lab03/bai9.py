while True:
	try:
		n = int(input('nhập n:'))
	except:
		print('mời nhập lại!!!')
	if n <= 0:
		print('mời nhập lại!!!')
	else:
		break
sum4 = 0
sum5 = 0
sum6 = 0
for i in range(n+1):
    sum4 += i**2 
    sum5 += (2*n+1)**3
    sum6 += (2*n)**4

print('S4=',sum4,'\nS5=',sum5,'\nS6=',sum6)
