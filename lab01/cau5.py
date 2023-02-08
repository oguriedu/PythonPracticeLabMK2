#a = [int(x) for x in input('Nhập vector a: ').split()]
#b = [int(x) for x in input('Nhập vector b: ').split()]
#result = sum(x * y for x, y in zip(a, b))
#print("Tích vô hướng của 2 vector là:", result)
#


a = [int(x) for x in input('Nhập vecto a: ').split()]
b = [int(x) for x in input('Nhập vecto b: ').split()]

if len(a) == len(b):  #Điều kiện để tính được tích vô hướng
    result = 0
    for i in range(len(a)): 
        result += a[i] * b[i]
    print('Tích vô hướng của 2 vecto là:',result)
else:
    print('Không thể tính được')
