number = int (input ('nhập số n: '))
def in_shh(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number
list_shh = []
for i in range(1,number):
    if in_shh(i):
        list_shh.append(i)
print ('danh sách các số hoàn hảo nhỏ hơn', number, 'là:', list_shh)

