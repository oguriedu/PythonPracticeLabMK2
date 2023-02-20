while True:
	try:
		n = int(input('nhập n:'))
	except:
		print('mời nhập lại!!!')
	if n <= 0:
		print('mời nhập lại!!!')
	else:
		break

sum1 = n*(1+n)/2
sum2 = (n+1)/2
sum3 = n*(n+1)
	
print('S1=',sum1)
print('S2=',sum2)
print('S3=',sum3)