x = int(input('nhập X:'))
y = int(input('Nhập Y:'))
val = [0]*x
for i in range(x):
    val[i] = [0] * y

for i in range(x):
    for j in range(y):
        val[i][j] = i*j

print(val)
