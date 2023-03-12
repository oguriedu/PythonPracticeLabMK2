number = int (input('enter the elements in Fi numbers: '))
Fi = [([0, 1]+Fi[i-1]+Fi[i-2]) for i in range(2, number)]
print('result =', Fi) 