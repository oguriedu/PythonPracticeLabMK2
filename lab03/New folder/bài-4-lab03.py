import math
n = int (input('nhập n: '))
def in_snt (number):
    if (number < 2):
        return False
    for i in range(2, int (math.pow(n, 0.5)) + 1):
        if (number % i == 0):
            return False
    return True

list_snt = []
if (n >= 2):
    list_snt.append(2)
for j in range(3, n + 1):
    if (in_snt(j)):
        list_snt.append(j)
    j = j+2
print ("tất cả các số nguyên tố nhỏ hơn ", n, "là: ", list_snt)