import random
A = []
while True:
    number = input('nhập các phần tử: ')
    if number == 'stop':
        break
    A.append(int(number))
print('list ban đầu: ', A)
B = [i for i in A if (i%3==0 and i%5!=0)]
print('list các số chia hết cho 3 nhưng k chia hết cho 5 =', B)
C = [(j**2) for j in A]
print('bình phương các phần tử trong list ban đầu =', C)
d = [k for k in A if (k%3==0)]
k = int (input('nhập số phần tử muốn lấy: '))
D = random.choices(d, k=k)
print('các phần tử ngẫu nhiên lấy từ list ban đầu chia hết cho 3 =', D)