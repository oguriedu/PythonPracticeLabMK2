a = [5, 10, 2]
b = [2, 4, 3]
dotproduct=0
for a,b in zip(a,b):
    dotproduct = dotproduct+a*b
print('Dot product is:', dotproduct)