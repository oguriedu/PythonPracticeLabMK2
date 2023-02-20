n = 5

for i in range(n):
    for j in range(n+1-i):
        print(' ',end='')
    for k in range(i+1):
        print('* ',end='')
    print('\n')

print('\n\n')
for i in range(n+1):
    for j in range(n+1-i):
        print('  ',end='')
    for k in range(i+1):
        print('*',end='   ')
    print('\n')


        
