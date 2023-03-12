n=int(input('Nhập n: '))
f = [0, 1]
[f.append(f[i-1] + f[i-2]) for i in range(2, n+1)]
print(*f,sep=',')