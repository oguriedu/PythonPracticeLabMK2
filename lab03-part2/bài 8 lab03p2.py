from tabulate import tabulate
n = int (input('nhập số nguyên dương n: '))
if n <= 0:
    print('nhập sai, mời nhập lại!!')
else:
    S1 = 0
    for i in range(n+1):
        S1 += i

    S2 = 0
    for j in range(n+1):
        S2 += 2*j+1

    S3 = 0
    for k in range(n+1):
        S3 += 2*n

list = []
list.append([S1, S2, S3])
name = ['S1', 'S2', 'S3']
print(tabulate(list, headers=name, tablefmt='fancy_grid'))